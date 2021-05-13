# 問題　解釈違い…最近多い…

import sys
h,w,k=map(int,input().split())
a=list(sys.stdin.read().split())
ans=0
for i in range(2**h-1):
    for j in range(2**w-1):
        cnt=0
        for y in range(h):
            if i>>(y)&1:
                continue
            for x in range(w):
                if j>>(x)&1:
                    continue
                if a[y][x]=="#":
                  cnt+=1
                
        if cnt==k:
            ans+=1
print(ans)


