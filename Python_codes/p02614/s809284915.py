h,w,k=map(int,input().split())
c=[input() for i in range(h)]
ans=0
for a in range(1<<h):
    for b in range(1<<w):
        cnt=0
        for i in range(h):
            if a>>i&1:
                continue
            for j in range(w):
                if b>>j&1:
                    continue
                cnt+=c[i][j]=='#'
        ans+=cnt==k
print(ans)