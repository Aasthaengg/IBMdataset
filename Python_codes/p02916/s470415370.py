n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

ans = sum(B)
ao=-1
for i in range(len(A)):
    if A[i]==ao+1 :
        ans+=C[A[i]-2]
    ao=A[i]
print(ans)
