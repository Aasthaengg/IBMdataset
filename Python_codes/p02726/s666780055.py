n,x,y = map(int,input().split())
ans = []
for i in range(n-1):
    ans.append(0)
for m in range(1,n):
    for a in range(1,n-m+1):
        d = abs(m - x)+ abs(m + a - y) +1
        if a <= d:
            ans[a-1] = ans[a-1] + 1
        else:
            ans[d-1] = ans[d-1] + 1
for l in ans:
    print(l)