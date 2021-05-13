n = int(input())
X = list(map(int, input().split()))

ans = float('inf')
for p in range(101):
    temp = 0
    for x in X:
        temp += (x-p)**2
    ans = min(ans, temp)
print(ans)
