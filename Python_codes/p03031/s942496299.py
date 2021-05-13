N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(M)]
p = list(map(int, input().split()))
ans=0
for i in range(2**N):
    a=[]
    flag=0
    for j in range(N):
        if (i>>j)&1:
            a.append(j+1)
    for k in range(M):
        cnt=0
        for l in range(A[k][0]):
            if A[k][l+1] in a:
                cnt+=1
        if cnt%2!=p[k]:
            flag=1
    if flag==0:
        ans+=1
    
print(ans)
