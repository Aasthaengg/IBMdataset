n = int(input())
d, x = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))

ans = x
day = 0
for e in A:
    while 1 + day * e <= d:
        day += 1
        ans += 1
    # print(day)
    day = 0
print(ans)
