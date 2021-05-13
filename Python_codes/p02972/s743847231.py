n = int(input())
ls = list(map(int,input().split()))
di = [100]*(n+1)
di[0] = 0
for i in range(n):
    N = n - i
    num = int(n/N)
    fi = []
    for j in range(num):
        fi.append(N*(j+1))
    p = 0
    for k in fi:
        p += di[k]
    if (p - 100)%2 == ls[fi[0]-1]:
        di[fi[0]] = 0
    else:
        di[fi[0]] = 1
print(sum(di))
for e in range(1,len(di)):
    if di[e] == 1:
        print(e,end=" ")