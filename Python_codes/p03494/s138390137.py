N=int(input())
A=list(map(int,input().split()))
M=int((max(A)**0.5)//1)
c=0
for i in range(M):
    for j in range(N):
        if A[j]%2==0:
            A[j]=int(A[j]//2)
            c+=1
        elif A[j]%2!=0:
            break
print(c//N)