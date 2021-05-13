from sys import stdin
N = int(stdin.readline().rstrip())
ans = float('inf')
for i in range(1, N):
    x = sum(int(c) for c in str(i))
    y = sum(int(c) for c in str(N-i))
    tmp = x + y
    ans = min(ans, tmp)
print(ans)