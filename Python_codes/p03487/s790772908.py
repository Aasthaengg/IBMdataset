N = int(input())
A = list(map(int,input().split()))
from collections import Counter
L = dict(Counter(A))
cnt = 0
for key,val in L.items():
    if key>val:
        cnt += val
    elif key<val:
        cnt += val-key
print(cnt)
