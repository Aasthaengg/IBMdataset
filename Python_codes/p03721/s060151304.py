N,K=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N)]

AB.sort()

cnt=0
for i in range(N):
    cnt+=AB[i][1]

    if cnt>=K:
        ans=AB[i][0]
        break

print(ans)