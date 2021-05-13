k,s=map(int,input().split())
c=0
for x in range(k+1):
 for y in range(k+1):
  c+=0<=s-x-y<=k
print(c)