n=int(input())
L0,L1=2,1
for i in range(n-1):
    L0,L1=L1,(L0+L1)
print(L1)