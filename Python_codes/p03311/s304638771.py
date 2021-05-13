N=int(input())
A=list(map(int,input().split()))

B=[0]*N

for i in range(N):
    B[i]=A[i]-(i+1)

B.sort()

b=[]
if N%2==1:
    b.append(B[(N+1)//2-1])
elif N%2==0:
    b.append(B[N//2-1])
    b.append(B[N//2])

ans=[]
for i in b:
    sum=0
    for j in range(N):
        sum+=abs(B[j]-i)
    ans.append(sum)

print(min(ans))