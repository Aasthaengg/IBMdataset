N=int(input())
A=list(map(int,input().split()))
a=len(set(A)) 
if (N-a)%2==1:
  print(a-1)
else:
  print(a)