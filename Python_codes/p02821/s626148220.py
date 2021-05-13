n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

scale = 20
h = 0
gauge = 2 ** scale
import bisect
while gauge > 0:
  h += gauge
  tmp = 0
  for i in range(n):
    b = bisect.bisect_left(a,h-a[i])
    tmp += n - b
  if tmp >= m:
    pass
  else:
    h -= gauge
  gauge //= 2
#print(h)

ans = 0
num = 0
cum = [0]
for i in range(n):
  cum.append(cum[-1]+a[-1-i])
cum.reverse()
for i in range(n):
  b = bisect.bisect_left(a,h-a[i])
  ans += cum[b]
  ans += a[i] * (n-b)
  num += n - b
  #print(b,ans,num)
ans -= (num-m) * h
#print(cum)
print(ans)