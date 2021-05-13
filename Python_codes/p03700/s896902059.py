n,a,b = [int(x) for x in input().split()]
c = a-b
h = []
for _ in range(n):
    h.append(int(input()))
h.sort()
m = h[-1]
z = 0
import bisect,math
while m-z>1:
    mid = (m+z)//2
    k = bisect.bisect_left(h,b*mid)
    cnt = 0
    for i in range(k,n):
        h2 = h[i]-b*mid
        cnt += math.ceil(h2/c)
    if cnt<=mid:
        m = mid
    else:
        z = mid

print(m)