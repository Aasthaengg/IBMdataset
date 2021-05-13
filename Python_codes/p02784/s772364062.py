import math

H, N = map(int, input().split())
A = list(map(int, input().split()))
ans = sum(A)
if ans >= H:
    print('Yes')
else:
    print('No')
