import sys

h,w,k=map(int,next(sys.stdin).split())
a=list(sys.stdin)

ans=0
for y in range(1<<h):
    for x in range(1<<w):
        ct=0
        for i in range(h):
            if y&(1<<i): continue
            for j in range(w):
                if x&(1<<j): continue
                ct+=a[i][j]=='#'
        ans+=ct==k

print(ans)
