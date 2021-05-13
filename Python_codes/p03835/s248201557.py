import sys
def S(): return sys.stdin.readline().rstrip()


K,S = map(int,S().split())

ans = 0
for i in range(K+1):
    for j in range(K+1):
        if 0 <= S-i-j <= K:
            ans += 1

print(ans)