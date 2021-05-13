import sys
K = int(input())
ans = 0
cur = 0
for i in range(10**6):
    cur += (7 * pow(10, i, K))%K
    if cur % K == 0:
        print(i+1)
        sys.exit()
    cur %= K
print(-1)