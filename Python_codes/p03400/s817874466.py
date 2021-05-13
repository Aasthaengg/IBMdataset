N=int(input())
D,X=map(int,input().split())
A=[]
cnt=0
for i in range(N):
    A.append(int(input()))
    
for i in range(N):
    for j in range(100):
        if A[i]*j+1 <= D:
            cnt+=1
print(cnt+X)