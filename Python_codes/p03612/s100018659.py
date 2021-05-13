import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
p = list(map(int, readline().split()))

ans = 0
ok = True
for i in range(n):
    if p[i] == i+1 and ok:
        ans += 1
        ok = False
    else:
        ok = True
print(ans)
