from statistics import median

N=int(input())
A=list(map(int,input().split()))
B=[]

for i in range(N):
    B.append(A[i]-i-1)
B.sort()

b=median(B)

ans=0
for i in range(N):
    ans+=abs(A[i]-b-i-1)

print(int(ans))