n,t = map(int,input().split())
tt = list(map(int,input().split()))
tt = [0]+tt
a = 0
for i in range(n):
  if(tt[i+1]-tt[i]>=t):
    a +=t
  else:
    a += tt[i+1]-tt[i]
print(a+t)