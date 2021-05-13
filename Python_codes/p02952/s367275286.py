n=int(input())
k=n
d=0
ans=0

while k>0:
  d+=1
  k=k//10

for i in range(d): #10**i~9999←i+1個
  if (i+1)%2==1:
    ans+=10**(i+1)-10**i
    

if d%2==1:
  ans=ans-(10**d-1-n)

print(ans)