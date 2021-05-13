import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,K = MI()

ans = 0
if K == 0:
    ans = N**2
else:
    for b in range(K+1,N+1):  # b を固定
        ans += N//b*(b-K) + max(0,N % b - (K-1))
print(ans)
