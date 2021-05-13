A, B, C=map(int,input().split())
K=int(input())
ab=int(A/B)
if ab==0:
  x=0
else:
  x=int(len(bin(ab))-2)
B1=B*(2**x)
bc=int(B1/C)
if bc==0:
  y=0
else:
  y=int(len(bin(bc))-2)
if x+y<=K:
  print("Yes")
else:
  print("No")