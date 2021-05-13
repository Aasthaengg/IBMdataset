N=int(input())
x,y = map(int,input().split())
p = list(map(int,input().split()))

a=0
b=0
c=0

for i in range(N):
  if p[i]<=x:
    a+=1
  elif p[i]>=y+1:
    c+=1
  else:
    b+=1

print(min([a,b,c]))