n, m = map(int,input().split())
s_list = []
p_list = []

for i in range(m):
    tmp = []
    tmp = list(map(int,input().split()))
    s_list.append(tmp)

p_list = list(map(int,input().split()))

ans = 0

for i in range((2**n)):
    bin_i = [int(x) for x in bin(i)[2:]]
    while len(bin_i) != n:
        bin_i.insert(0,0)
    flag = 0
    for j in range(m):
        tmp = 0
        for k in range(1,s_list[j][0]+1):
            tmp += bin_i[s_list[j][k]-1]
        if tmp%2 != p_list[j]:
            flag = 1
            break
    if flag == 0:
        ans += 1

print(ans)
