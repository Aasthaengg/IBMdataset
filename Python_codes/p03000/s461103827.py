N, X = map(int, input().split())
L = list(map(int, input().split()))
ans = 1
now = 0
for i in range(N):
    if now + L[i] <= X:
        ans += 1
        now += L[i]
    else:
        break
print(ans)
