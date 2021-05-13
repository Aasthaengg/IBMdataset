import sys
n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = sum(a)
node = 1

for i in range(n + 1):
    ans += node
    cnt -= a[i]
    node = min(cnt, (node - a[i]) * 2)

    if node < 0:
        print(-1)
        sys.exit()

print(ans)