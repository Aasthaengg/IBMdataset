n, k = map(int, input().split())
hitpoints = list(map(int, input().split()))

hitpoints.sort(reverse=True)
del hitpoints[:k]

ans = 0
for i in hitpoints:
    ans += i

print(ans)