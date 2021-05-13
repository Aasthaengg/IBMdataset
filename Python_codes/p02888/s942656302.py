import bisect
n,*l = map(int,open(0).read().split())
l.sort()
ans = 0
for i in range(n-2):
  for j in range(i+1,n-1):
    ans += bisect.bisect_left(l,l[i]+l[j],j+1)-bisect.bisect_right(l,abs(l[i]-l[j]),j+1)
print(ans)