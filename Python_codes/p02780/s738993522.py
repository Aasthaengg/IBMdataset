N,K = map(int,input().split())
p = [int(x) for x in input().split()]

cnt = 0

for i in range(K):
    cnt += p[i]
ans = cnt
for i in range(1,N-K+1):
    cnt -= p[i-1]
    cnt += p[K+i-1]
    ans = max(cnt,ans)


print((ans+K)/2)