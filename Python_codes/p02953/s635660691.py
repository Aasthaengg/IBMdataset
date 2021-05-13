N=int(input())
H=list(map(int,input().split()))

C=[H[0]]
for i in range(1,N):
    if H[i-1]!=H[i]:
        C.append(H[i])
        
for i in range(len(C)-1):
    if C[i]>C[i+1]:
        C[i]-=1

F=True
for i in range(len(C)-1):
    F&=(C[i]<=C[i+1])

if F:
    print("Yes")
else:
    print("No")
