N = int(input())
X = [None]*N
a = 0
for i in range(N):
    A, B = map(int, input().split())
    X[i] = (A+B, A, B)
X.sort(reverse=1)
ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += X[i][1]
    else:
        ans -= X[i][2]
print(ans)