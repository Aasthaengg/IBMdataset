a,b,c = map(int,input().split())
k = int(input())
while(k>0):
  if b>a:
    break
  b*=2
  k-=1
while(k>0):
  if c>b:
    break
  c*=2
  k-=1
print("Yes" if c>b and b>a else "No") 