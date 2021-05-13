import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

s = readline().decode()
ans = s.count('+')-s.count('-')
print(ans)
