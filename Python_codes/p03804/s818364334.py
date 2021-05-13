N,M=map(int,input().split())
A=[]
B=[]
for i in range(N):
    A.append(input())
for i in range(M):
    B.append(input())

for i in range(N-M+1):
    for j in range(N-M+1):
        f=True
        for k in range(M):
            if A[j+k][i:M+i]==B[k]:continue
            else:
                f=False
                break
        if f:
            print("Yes")
            exit()
print("No")
