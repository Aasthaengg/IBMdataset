from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
b.sort()
c.sort()
ans = 0

bcb_cum = [0] * (n+1)
for i in range(n):
    bcb_cum[i+1] = bcb_cum[i] + n - bisect_right(c, b[i])
    
for x in a:
    l = bisect_right(b, x)
    ans += bcb_cum[n] - bcb_cum[l]

print(ans)
