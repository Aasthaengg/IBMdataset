N=int(input())
L=[0]
for i in range(30):
  L+=[i+4 for i in L]+[i+7 for i in L]
  L=list(set(L))
if N in L:
  print("Yes")
else:
  print("No")