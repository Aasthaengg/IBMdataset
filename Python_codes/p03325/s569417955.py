n=int(input())
r=list(map(int,input().split()))
c=0
for x in r:
  while x%2==0:
    x//=2
    c+=1
print(c)