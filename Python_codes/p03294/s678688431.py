import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int, readline().split()))
ans = 0
for v in a:
    ans += v-1

print(ans)