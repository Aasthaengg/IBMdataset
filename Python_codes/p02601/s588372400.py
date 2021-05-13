A,B,C=map(int,input().split())
K=int(input())
d=0
for i in range(K):
  if A>=B:
    B=B*2
  elif B>=C:
    C=C*2
if( B>A and C>B):print("Yes")
else:print("No")