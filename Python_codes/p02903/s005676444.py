h,w,a,b=map(int,input().split())

ans=[[0]*w for _ in range(h)]

for r in range(h):
    for c in range(w):
        if (0<=r<b and 0<=c<a) or (b<=r<h and a<=c<w):
            ans[r][c]+=1
    
    print(''.join([str(c) for c in ans[r]]))