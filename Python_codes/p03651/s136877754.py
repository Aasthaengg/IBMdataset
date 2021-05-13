n,k=map(int,input().split())
l=sorted(map(int,input().split()))
def gcd(x,y):
  if y==0:return x
  return gcd(y,x%y)
ans=""
s=0
for i in l:
  s=gcd(i,s)
  if s==1:break
else:
  if k%s!=l[-1]%s:
    ans="IM"
if l[-1]<k:ans="IM"
print(ans+"POSSIBLE")
