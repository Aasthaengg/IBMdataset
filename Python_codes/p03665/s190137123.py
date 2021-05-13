n, p = map(int, input().split())
A  = list(map(int, input().split()))

N = 10**3
C = [[0]*(N+1) for i in range(N+1)] #C[n][k] > nCk

for i in range(N+1):
    for j in range(i+1):
        if j == 0 or j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i-1][j-1]+C[i-1][j]

def cmb3(n, k):
    return C[n][k]

e = 0
o = 0
for a in A:
    if a%2 == 0:
        e += 1
    else:
        o += 1

if p == 0:
    ans = 0
    for i in range(o+1):
        if i%2 == 1:
            continue
        else:
            ans += cmb3(o, i)
    ans *= 2**e
    print(ans)
else:
    ans = 0
    for i in range(o+1):
        if i%2 == 0:
            continue
        else:
            ans += cmb3(o, i)
    ans *= 2**e
    print(ans)
