n,k = map(int,input().split())
if k > (n-1)*(n-2)/2:
    print(-1)
else:
    ans = []
    for i in range(1,n):
        ans.append([1,i+1])
    L = []
    for i in range(2,n+1):
        for j in range(i+1, n+1):
            L.append([i,j])
    for i in range((n-1)*(n-2)//2-k):
        ans.append(L[i])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
