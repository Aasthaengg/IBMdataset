n = int(input())
colors = list(map(int, input().split()))

cnt = 0
for r in range(n-1):
    if colors[r] == colors[r+1]:
        cnt += 1
        colors[r+1] = '*'

print(cnt)