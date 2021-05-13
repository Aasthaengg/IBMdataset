N,M=map(int,input().split())
ls3 = []
for i in range(M):
    ls1=list(map(int,input().split()))
    ls1.pop(0)
    ls3.append(ls1)
ls2 = list(map(int,input().split()))

kk = 0
for i in range(2**N):
    ls4 = [0]*M
    for j in range(N):
        if (i>>j&1):
            for k in range(M):
                if j+1 in ls3[k]:
                    ls4[k] += 1
    ii = 0
    for l in range(M):
        if ls4[l] % 2==ls2[l]:
            ii += 1

    if ii == M:
        kk += 1
print(kk)