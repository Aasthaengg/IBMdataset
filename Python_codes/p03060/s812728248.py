n=int(input())

v=list(map(int,input().split()))
c=list(map(int,input().split()))

sm=0
for i in range(n):
  x=v[i]-c[i]
  if x>0:
    sm+=x
print(sm)  