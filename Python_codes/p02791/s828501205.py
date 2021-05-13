n=int(input())
A=list(map(int,input().split()))
cnt=0
x=A[0]
for i in range(n):
    if A[i]<=x:
        cnt+=1
        x=min(x,A[i])
print(cnt)