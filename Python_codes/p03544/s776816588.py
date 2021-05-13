a=int(input())
L=2
L1=1
L2=0
for i in range(a):
  L2=L+L1
  L=L1
  L1=L2
print(L)  