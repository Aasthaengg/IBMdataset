N,K=map(int,input().split())
m=lambda x:x*(x-1)//2
M=lambda x:x*N-x*(x-1)//2
res=0
p=10**9+7
for k in range(K,N+2):
    res+=(M(k)-m(k)+1)%p
print(res%p)