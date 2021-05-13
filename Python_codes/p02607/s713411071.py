N=int(input())
A=list(map(int,input().split()))
s=0
for i in range(0,N,2):
    if A[i]%2 !=0:
        s=s+1
print(s)