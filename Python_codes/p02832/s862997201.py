N=int(input())
A=list(map(int,input().split()))

count=0
k=1
for i in range(len(A)):
    if A[i]==k:
        count+=1
        k+=1

if count==0:
    print(-1)
else:
    print(len(A)-count)