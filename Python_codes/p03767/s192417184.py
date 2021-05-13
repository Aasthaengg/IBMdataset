N = int(input())
a = sorted([int(x) for x in input().split()], reverse=True)

ans = 0
for i in range(N):
    ans += a[2 * i + 1]

print(ans)