a,b,k=map(int,input().split())
s=[a,b]
for i in range(k):
  x,y=int((1-(-1)**i)/2),int((1+(-1)**i)/2)
  if s[x]%2==1:
    s[x]-=1
  s[y]+=s[x]//2
  s[x]-=s[x]//2
print(s[0],s[1])