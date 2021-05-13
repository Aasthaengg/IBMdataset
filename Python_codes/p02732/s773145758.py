N=int(input())
A=list(map(int,input().split()))
B=[0]*(N+1)
C=0
for i in A:
    B[i-1]+=1
for i in B:
    if i>=2:
        C+=i*(i-1)//2
for i in A:
    print(C-B[i-1]+1)
