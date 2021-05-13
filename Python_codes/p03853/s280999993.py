H,W=map(int,input().split())
L=[[] for i in range(2*H)]
for i in range(H):
  L1=list(input())
  L[2*i]=L1
  L[(2*i)+1]=L1
for i in range(2*H):
  print("".join(L[i]))