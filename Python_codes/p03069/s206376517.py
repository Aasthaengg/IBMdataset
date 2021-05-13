N=int(input())
S=list(map(int,input().replace('#','1').replace('.','0')))
 
cum=[0]
for i in range(N):
  cum.append(cum[-1]+S[i])
  
ans=10**20
for i in range(N+1):
  b = cum[i]
  w = N-i-(cum[-1]-cum[i])
  ans = min(ans,b+w)
  
print(ans)