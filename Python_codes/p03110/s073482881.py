import sys
inp = sys.stdin.buffer.readline

ans = 0
N = int(inp())
for i in range(N):
    X = list(input().split())
    if X[1] == 'JPY':
        ans += int(X[0])
    else:
        ans += 380000 * float(X[0])
print(ans)