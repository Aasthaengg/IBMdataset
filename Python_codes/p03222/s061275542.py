mod = 10**9+7
h, w, k = [ int(v) for v in input().split() ]

non_contiuous_list = [1,2]

end_0, end_1 = 1, 1
for i in range(8):
    end_1_new = end_0
    end_0_new = end_0 + end_1
    end_0, end_1 = end_0_new, end_1_new
    non_contiuous_list.append(end_0 + end_1)


def non_contiuous(x):
    global non_contiuous_list
    if x >= 0:
        return non_contiuous_list[x]
    else:
        return 1

reach = [ [ 0 for i in range(w) ] for j in range(h+1) ]
reach[0][0] = 1

for i in range(1,h+1):
    if w > 1:
        for j in range(w):
            a = max(0,w-2)
            b = max(0,w-3)
            if j == 0:
                reach[i][j] = reach[i-1][j] * non_contiuous(a) + reach[i-1][j+1] * non_contiuous(b)
            elif j == w - 1:
                reach[i][j] = reach[i-1][j] * non_contiuous(a) + reach[i-1][j-1] * non_contiuous(b)
            else:
                reach[i][j] = reach[i-1][j-1] * non_contiuous(j-2) * non_contiuous(w-j-2) + reach[i-1][j] * non_contiuous(j-1) * non_contiuous(w-j-2) + reach[i-1][j+1] * non_contiuous(j-1) * non_contiuous(w-j-3) 
    else:
        reach[i][0] = 1

    reach[i] = [ j % mod for j in reach[i] ] 

print(reach[h][k-1])