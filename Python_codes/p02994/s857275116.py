n, l = map(int, input().split())
taste = [l+i for i in range(n)]

tmp = float('inf')
sum = sum(taste)
for i in range(n):
    if abs(taste[i]) < tmp:
        tmp = abs(taste[i])
        ans = sum - taste[i]

print(ans)
