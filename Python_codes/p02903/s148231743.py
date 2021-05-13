h,w,a,b = map(int, input().split())
ans=[]
for i in range(h):
    if i<b:
        ans.append([0]*w)
    else:
        ans.append([1]*w)
for i in range(h):
    for j in range(w):
        if j<a:
            ans[i][j] = (ans[i][j] + 1)%2
for a in ans:
    print(*a,sep="")