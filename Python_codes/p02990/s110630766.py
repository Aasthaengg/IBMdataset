def combi(a,b):
  s=fac[a]
  t=fac[b]        
  u=fac[a-b]
  ans = ( s*pow(t,p-2,p)*pow(u,p-2,p) )%p
  return ans
############################################ 
N,K=map(int,input().split())
p=10**9+7
fac=[1,1]
for i in range(2,N+1):
  a= fac[-1]*i % p
  fac.append(a)
    
for i in range(1,K+1):
  if N-K < i-1:
    #print("err")
    ans=0
  else:
    q= N-K-(i-1) #ボールの数
    r = i #仕切りの数
    ans = ( combi(K-1,i-1)*combi(q+r,q) )%p
    #print(1,combi(K-1,i-1),combi(q+r,q))
  print(ans)