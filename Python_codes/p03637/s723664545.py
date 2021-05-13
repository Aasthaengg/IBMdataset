n=int(input())
A=list(map(int,input().split()))
Q=[a for a in A if a%4==0]
W=[a for a in A if a%4==2]
if len(Q)>=n//2:
  print("Yes")
else:
  if len(W)>=n-len(Q)*2:
    print("Yes")
  else:
    print("No")