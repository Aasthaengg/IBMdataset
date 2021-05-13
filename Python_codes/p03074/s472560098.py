# solution

nim,mike=map(int,input().split())
data=input()
X=[]
Y=[0]
_s='2'
for i,s in enumerate(data):
  if _s!=s:
    _s=s
    X.append(i)
    Y.append((int(s)+1)%2)
import itertools
Y=list(itertools.accumulate(Y))
ans=[]
for i,x in enumerate(X):
  if Y[-1]-Y[i]<=mike:
    ans.append(nim-x)
    break
  else:
    if data[x]=='0':
      ans.append(X[i+2*mike]-x)
    else:
      ans.append(X[i+2*mike+1]-x)
print(max(ans))