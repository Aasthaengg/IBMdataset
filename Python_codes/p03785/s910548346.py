N, C, K=map(int, input().split())
X=[]
for _ in range(N):
  X.append(int(input()))
X.sort()
X.append(10**19)
ans=0
tamatta=0
hayaihito=X[0]
for i in range(N+1):
  if tamatta<C and hayaihito+K>=X[i]:
    tamatta+=1
  else:
    ans+=1
    tamatta=1
    hayaihito=X[i]
    
print(ans)