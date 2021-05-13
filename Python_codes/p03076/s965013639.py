def mi(): return map(int,input().split())
def lmi(): return list(map(int,input().split()))
def ii(): return int(input())
def isp(): return input().split()

a=[]
r=[]
for i in range(5):
  s=ii()
  a.append(s)
  r_=s%10
  if r_==0:
    r_=10
  r.append(r_)
  
ans=0
while len(r)>1:
  k=r.index(max(r))
  remain=r.pop(k)
  A=a.pop(k)
  #print(A)
  ans+=A-remain+10
  
print(ans+a[0])