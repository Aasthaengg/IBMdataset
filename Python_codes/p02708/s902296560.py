N,K = map(int,input().split())
mod = pow(10,9)+7
c = 0
cnt = 0
for i in range(K,N+1):
    temp1 = 0.5*(K+cnt)*(K+cnt-1)
    temp2 = (K+cnt)*0.5*(2*N-(K+cnt-1))
    c += temp2 - temp1 + 1
    c = c%mod
    cnt += 1
c += 1
print(int(c))