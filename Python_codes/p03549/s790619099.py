N,M=map(int, input().split())
#M*1900  (0.5)**M  (N-M)*100
ans=0
p=1
for i in range(10**5):
  ans+=(i+1)*(M*1900+(N-M)*100)* (p*((0.5)**M))
  p*=(1-(0.5)**M)
  #print(ans)
  
  #print(p)
  
print(round(ans))