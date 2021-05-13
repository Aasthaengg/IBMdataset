N=int(input())
A=[]
A=list(map(int,input().split()))
ans=[0 for i in range(N)]
for i in range(N-1):
    ans[A[i]-1]=ans[A[i]-1]+1

for i in ans:
    print(i)
