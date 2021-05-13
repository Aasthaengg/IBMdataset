N, K = map(int, input().split()) 
cnt = 0
for i in range(1, N+1):
    p = N//i
    q = N%i
    cnt += p*max(0, i-K)
    cnt += max(0, q-K+1)
if K == 0:
    cnt -= N
print(cnt)