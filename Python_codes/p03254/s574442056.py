n,x = map(int,input().split())
kids = list(map(int,input().split()))

kids.sort()
i=0
while i<n and x>=kids[i]:
  x-=kids[i]
  i+=1

if x!=0 and i==n:
  i-=1
if i<0:
  i=0
  
print(i)