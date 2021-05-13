from sys import stdin

n = int(stdin.readline().rstrip())
m = [stdin.readline().rstrip().split() for _ in range(n)]
ans = 0
for mi in m:
    ans += int(mi[1]) + 1 - int(mi[0])

print(ans)