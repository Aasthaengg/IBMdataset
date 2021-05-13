N,M = map(int, input().split())
S = [0]*M; C = [0]*M
for i in range(M):
    S[i], C[i] = map(int, input().split())

for i in range(M):
    s,c = S[i],C[i]

if N == 1:
    Range = range(0,10)
else:
    Range = range(10**(N-1), 10**N)
for x in Range:
    z = str(x)
    flag = True
    for i in range(M):
        s,c = S[i],C[i]
        if s <= len(z):
            if z[s-1] != str(c):
                flag = False
                break
        else:
            flag = False
            break
    if flag:
        print(z)
        exit()
print(-1)