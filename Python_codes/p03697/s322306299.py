import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b = map(int, readline().split())
ans = a+b if (a+b) < 10 else 'error'
print(ans)