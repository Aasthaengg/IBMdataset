import sys

N = int(sys.stdin.readline().strip())

data = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    data.append((a, b))

ans = 0
adds = 0
for i in range(N):
    a, b = data[N-1-i]
    a += adds
    r = (a - 1) // b
    target = b * (r + 1)
    tmp = target - a
    ans += tmp
    adds += tmp

print(ans)