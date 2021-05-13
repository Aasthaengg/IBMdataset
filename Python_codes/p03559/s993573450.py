n = int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
import bisect
ans = 0
for i in range(n):
    abis = bisect.bisect_left(a, b[i])
    cbis = bisect.bisect_right(c, b[i])
    ans += abis*(n-cbis)
print(ans)


