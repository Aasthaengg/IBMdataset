N=int(input())
*A1,=map(int,input().split())
*A2,=map(int,input().split())

ans=[0]*N
i=0
while i<N:
    ans[i]+=sum(A1[:i+1])
    ans[i]+=sum(A2[i:])
    i+=1

print(max(ans))