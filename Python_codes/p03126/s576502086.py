import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m = map(int, readline().split())
ka = []
ans = set(str(i+1) for i in range(m))

for _ in range(n):
    ka = input().split()
    ans = ans & set(ka[1:])
    
print(len(ans))