import sys
N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
a=0
b=0
c=0
for x in range(N):
  if P[x]<=A:
    a+=1
  elif P[x]>A and P[x]<=B:
    b+=1
  elif P[x]>B:
    c+=1
  else:
    sys.stderr.write("error")
print(min(a,b,c))