N=int(input())
*A,=sorted(map(int,input().split()))

import bisect

for i in range(1,N+1):
    print(bisect.bisect_right(A,i)-bisect.bisect_left(A,i))