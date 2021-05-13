import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c = map(int, readline().split())
ans = 'Yes' if a <= c <= b else 'No'
print(ans)