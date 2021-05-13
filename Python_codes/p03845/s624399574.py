N=int(input())
T=list(map(int,input().split()))
M=int(input())
total=sum(T)
ans=[0 for i in range(M)]
for i in range(M):
    p,x=map(int,input().split())
    ans[i]=total-T[p-1]+x

for an in ans:
    print(an)