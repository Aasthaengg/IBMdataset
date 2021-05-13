from sys import stdin
N,K = [int(x) for x in stdin.readline().rstrip().split()]
ans = 0
for b in range(1,N+1):
    p = N//b
    ans += p*max(b-K,0)
    r = N % b
    ans += max(r-K+1,0)
if K == 0:
    ans = N**2
print(ans)