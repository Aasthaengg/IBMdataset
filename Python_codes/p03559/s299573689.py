n=int(input())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
c=sorted(list(map(int,input().split())))

import bisect

ans=0
for i in range(n):
    num_a=bisect.bisect_left(a,b[i])
    idx_c=bisect.bisect_right(c,b[i])
    num_c=n-idx_c
    ans+=num_a*num_c
print(ans)

