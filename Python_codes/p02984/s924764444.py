n = int(input())

rains = list(map(int, input().split()))

start = 0

for i in range(n):
    if i%2:
        start -= rains[i]

    else:
        start += rains[i]

ans = start
print(start, end=' ')
for i in range(n-1):
    ans = 2 * rains[i] - ans
    print(ans, end=' ')