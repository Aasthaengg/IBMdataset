#64 C - Good Sequence
import collections
N = int(input())
A = list(map(int,input().split()))

cnt = collections.Counter(A)

ans = 0
for key,value in cnt.items():
    if key > value:
        ans += value
    if value > key:
        ans += (value - key)
print(ans)