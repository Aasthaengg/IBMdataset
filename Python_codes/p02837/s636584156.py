n = int(input())

l = []
aas = []

for i in range(n):
    a = int(input())
    aas.append(a)
    s = [list(map(int,input().split())) for i in range(a)]
    l.append(s)

for i in range(2**n):
    flag_n = [1]*n
    for j in range(n):
        if ((i >> j)&1):
            flag_n[n-1-j] = 0
    cnt = 0
    for k in range(n):
        if flag_n[k] == 1:
            if all(l[k][m][1] == flag_n[l[k][m][0]-1] for m in range(aas[k])):
                cnt += 1
        if cnt == sum(flag_n):
            print(sum(flag_n))
            exit()

print(0)
        
