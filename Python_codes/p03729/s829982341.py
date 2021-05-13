import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c = read().decode().split()
ans = 'YES' if a[-1] == b[0] and b[-1] == c[0] else 'NO'
print(ans)