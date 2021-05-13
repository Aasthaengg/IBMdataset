N, X = map(int, input().split())
L = list(map(int, input().split()))
a = 0
ans = N + 1
for i in range(N):
    a += L[i]
    if a > X:
        ans = i + 1
        break
print(ans)