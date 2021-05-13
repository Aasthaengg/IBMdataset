n, x = map(int, input().split())
l = list(map(int, input().split()))

bound = [0]
for i in range(n):
    bound.append(bound[i] + l[i])

ans = 0
for j in range(n+1):
    if bound[j] <= x:
        ans += 1
print(ans)
