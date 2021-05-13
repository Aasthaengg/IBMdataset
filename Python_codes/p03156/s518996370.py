N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
  
s=0
t=0
u=0
  
for q in P:
  if q<=A:
    s += 1
  elif A+1<=q<=B:
    t += 1
  else:
    u += 1
print(min(s,t,u))