from itertools import accumulate
N = int(input())
a = tuple(map(int,input().split()))
s = list(accumulate(a))
b = [0]*(N+1)
if N == 0 and a[0] > 1:
    print(-1)
    exit()
if a[0] == 0:
    b[0] = 1
ans = 1
flag = 0
for d in range(1,N+1):
    b[d] = b[d-1]-a[d]
    tmp = min(s[-1]-s[d],2*b[d-1]-a[d])
    if b[d] > tmp or tmp < 0:
        flag = 1
        break
    else:
        b[d] = tmp
if flag:
    print(-1)
else:
    print(s[-1]+sum(b))