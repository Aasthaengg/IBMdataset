K, X = map(int, input().split())

left = X - K + 1
right = X + K - 1
ans = []

for i in range(left, right+1):
    ans.append(i)

print(*ans)
