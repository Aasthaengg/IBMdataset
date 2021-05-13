import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a = sorted(map(int, readline().split()))
ans = (a[2]-a[1])+(a[1]-a[0])
print(ans)
