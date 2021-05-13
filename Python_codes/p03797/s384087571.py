import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int,readline().split())

if n >= m//2:
    print(m//2)
    exit()

ans = n
m -= n*2

ans += m//4
print(ans)