import sys
N, K = map(int, input().split())

ans = 0

for i in range(1,N+1,2):
    ans = ans + 1

if ans >= K:
    print("YES")
    sys.exit()

print("NO")
