L=[[0 for j in range(3)] for i in range(3)]
for i in range(3):
  c=list(map(int,input().split()))
  L[i]=c
if L[0][0]-L[1][0]==L[0][1]-L[1][1]==L[0][2]-L[1][2] and L[0][0]-L[2][0]==L[0][1]-L[2][1]==L[0][2]-L[2][2]:
  print("Yes")
else:
  print("No")