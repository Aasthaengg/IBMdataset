import sys
input = sys.stdin.readline
from collections import *

K, A, B = map(int, input().split())

if A>=B:
    print(K+1)
else:
    if B-A==1:
        print(K+1)
    else:
        if A-1>=K:
            print(K+1)
        else:
            rem = K-(A-1)
            ans = A+(B-A)*(rem//2)
            
            if rem%2==1:
                ans += 1
            
            print(ans)