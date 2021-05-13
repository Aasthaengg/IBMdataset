import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = list(read().decode().split())
ans = (s[0][0] + s[1][0] + s[2][0]).upper()
print(ans)