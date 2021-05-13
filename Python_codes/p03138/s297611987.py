N, K = map(int, input().split())
L = K.bit_length()
D = [0]*(L+1)
A = list(map(int, input().split()))
res=0
for a in A:
    for i in range(L+1):
        D[i] += (a>>i)&1
for i in reversed(range(L+1)):
    if D[i]*2<=N and res+(1<<i)<=K:
        res+=(1<<i)
print(sum(a^res for a in A))
