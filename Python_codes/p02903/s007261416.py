h,w,a,b = map(int,input().split())
ans = [["0"]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if (w-a<=j and h-b>i) or (w-a>j and h-b<=i):
            ans[i][j] = "1"
for i in range(h):
    print("".join(ans[i]))