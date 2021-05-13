N, X = map(int, input().split())
L = list(map(int, input().split()))
ans = 1
now = 0
for i in range(N):
    now += L[i]
    if now <= X:
        ans += 1
    else:
        break
print(ans)
