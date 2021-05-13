N,K = map(int,input().split())
ans = 0
for b in range(K+1,N+1):
    Q = N//b
    R = N%b
    ans += Q*(b-K)+max(0,R+1-K)
if K == 0:
    ans = N**2
print(ans)
