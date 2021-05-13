n, a, b = map(int, input().split())
V = list(map(int, input().split()))
V.sort(reverse=True)

N = 50
C = [[0]*(N+1) for i in range(N+1)] #C[n][k] > nCk

for i in range(N+1):
    for j in range(i+1):
        if j == 0 or j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i-1][j-1]+C[i-1][j]

def comb3(n, k):
    return C[n][k]

ans = 0
x = 0
y = 0
for i in range(n):
    if i <= a-1:
        ans += V[i]
        if V[i] == V[a-1]:
            x += 1
            y += 1
    else:
        if V[i] == V[a-1]:
            x += 1

if V[0] != V[a-1]:
    cnt = comb3(x, y)
    print(ans/a)
    print(cnt)
else:
    cnt = 0
    for i in range(a, b+1):
        if i <= x:
            cnt += comb3(x, i)
    print(ans/a)
    print(cnt)
