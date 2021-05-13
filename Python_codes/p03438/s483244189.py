N=int(input())

A=list(map(int, input().split()))
B=list(map(int, input().split()))
K=sum(B)-sum(A)
if K<0:
    print("No")
    exit()

#合計値が追い越さないように　sum(B)-sum(A)回までしかできない

anum=0
bnum=0
for i in range(N):
    a=A[i]
    b=B[i]
    if a>b:
        bnum+=a-b
    elif b>a:
        if (b-a)%2==0:
            anum+=(b-a)//2
        else:
            anum+=(b-a)//2+1
            bnum+=1

if K>=max(anum,bnum):
    print("Yes")
else:
    print("No")