N,K= map(int,input().split())
p=10**9+7
q=0
 
def calc(n,k):
  if k==1:
    return n+1
  else:
    maxi = k*n- k*(k-1)//2
    mini=  k*(k-1)//2
    #print(k,maxi,mini,maxi-mini+1)
    return maxi-mini+1
  
ans=0
for i in range(K,N+2):
  ans = ( ans+calc(N,i) )%p
  
print(ans)
