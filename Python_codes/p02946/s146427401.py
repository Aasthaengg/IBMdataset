K,X=map(int,input().split())
ans=list()
init=X-(K-1)
for i in range(2*K-1):
    ans.append(init)
    init+=1
print(*ans)