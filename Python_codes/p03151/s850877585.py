n= int(input())
*a,=map(int, input().split( ))
*b,=map(int, input().split( ))
ab = [a[i]-b[i] for i in range(n)]
if sum(ab)<0:
    print(-1)
    exit()

ab.sort()
import bisect
j = bisect.bisect_left(ab,0)
minus = sum(ab[:j])

ans = 0
while minus<0:
    abi = ab.pop()
    minus += abi
    ans += 1
print(ans+j)