N=int(input())
C_max=N//4
D_max=N//7
M=0

for i in range(C_max+1):
    for j in range(D_max+1):
        if N== 4*i+7*j:
            M+=1
if M==0:
    print("No")
else:
    print("Yes")