N,x=map(int,input().split())
A=list(map(int,input().split()))
A.sort()

K=0
for i in range(N-1):
    if x>=A[i]:
        x-=A[i]
        K+=1

if x==A[-1]:
    K+=1

print(K)
