N=int(input())
A=list(map(int,input().split()))

from collections import Counter
A_=Counter(A)

A_key=list(A_.keys())
A_key.sort()

ans=0
for k in A_key:
    if k > A_[k]:
        ans += A_[k]
    else:
        ans += A_[k]-k
print(ans)