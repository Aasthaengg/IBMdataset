n,k=map(int,input().split())
s=input()
p2=0
p1=0
if n==1:
  print(0)
  exit()
if s[0]=="L":
  p1+=1
if s[n-1]=="R":
  p1+=1
  
for i in range(1,n):
  if not (s[i]=="L" and s[i-1]=="R"):
    continue
  p2+=1
if k<=p2-1:
  print(n-2*p2-p1+2*k)
elif p2-1<k<p2+p1:
  print(n-p1+(k-p2))
else:
  print(n-1)
