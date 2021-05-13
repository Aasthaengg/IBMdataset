import sys
N, K = map(int, input().split())
a = sorted([int(input()) for i in range(N)])

ans = 10**10
for i in range(N-K+1):
    ans = min(ans, a[i+K-1]-a[i])
    if ans == 0:
        print(0)
        sys.exit()
print(ans)
