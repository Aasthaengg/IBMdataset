N=int(input())
A=[]
B=[]
ans=0
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

for i in range(N):
    ans+=(B[(-1)*(i+1)]-(A[(-1)*(i+1)]+ans))%B[(-1)*(i+1)]
print(ans)
