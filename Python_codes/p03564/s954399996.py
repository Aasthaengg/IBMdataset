import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k = [int(readline()) for _ in range(2)]
ans = 1
for i in range(n):
    ans = min(ans * 2, ans + k)
print(ans)