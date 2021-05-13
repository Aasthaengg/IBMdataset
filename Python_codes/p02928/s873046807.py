N,K=list(map(int,input().split()))
n_l=list(map(int,input().split()))
ans=0
mod=10**9+7
for i in range(N):
   A=n_l[i]
   ans+=len([j for j in n_l[i+1:] if j < A])
ans2=0
for i in n_l:
   ans2+=len([k for k in n_l if i > k])
f_a=ans*K%mod+K*(K-1)//2*ans2%mod
print(f_a%mod)