import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

c1, c2 = [list(readline().decode().rstrip()) for _ in range(2)]
ans = 'YES' if c1 == c2[::-1] and c2 == c1[::-1] else 'NO'
print(ans)