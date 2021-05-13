#abc104c all green 
d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]
all_sum = []
for bit in range(1<<d):
    s = 0
    a = 0
    rest = []
    for i in range(d):
        if bit & (1<<i):
            s += pc[i][0]*100*(i+1) + pc[i][1]
            a += pc[i][0]
        else :
            rest.append(i)
    
    if s >= g :
        all_sum.append(a)
    else :
        k = max(rest)
        diff = g - s
        for j in range(pc[k][0]):
            if j*(k+1)*100 >= diff:
                all_sum.append(a+j)
print(min(all_sum))