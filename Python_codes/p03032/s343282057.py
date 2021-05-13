N,K = map(int,input().split())
V = list(map(int,input().split()))
ans = 0
for i in range(1,min(N,K)+1):#i個とる
    for j in range(-i,1):
        lis = []
        for k in range(i):
            lis.append(V[j+k])
            #print(i,j,k,j+k)
        lis.sort(reverse=True)
        cnt = 0
        while (len(lis) != 0 and i+cnt < K and lis[-1] < 0):
            del lis[-1]
            cnt += 1
        ans = max(ans,sum(lis))
print(ans)
