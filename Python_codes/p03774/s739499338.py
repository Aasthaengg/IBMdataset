N,M=map(int,input().split())
stu=[list(map(int,input().split()))for i in range(N)]
zahyou=[list(map(int,input().split()))for i in range(M)]
ans=list()
for i in range(N):
    tmp=10**10
    tmp2=0
    for j in range(M):
        dist=abs(stu[i][1]-zahyou[j][1])+abs(stu[i][0]-zahyou[j][0])
        if dist <tmp:
            tmp=dist
            tmp2=j+1
    ans.append(tmp2)        
for i in ans:
    print(i)

