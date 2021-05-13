N=int(input())
A=list(map(int,input().split()))
B=[0]*(N)

S=0
p=1
for i in range(N):
    S+=A[i]*p
    p*=-1


for i in range(N):
    B[i]=S

    S*=-1
    S+=2*A[i]

print(" ".join(map(str,B)))