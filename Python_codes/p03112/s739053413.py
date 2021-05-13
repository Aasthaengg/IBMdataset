import bisect
inf = 10**18
a, b, q = map(int, input().split())
s = []
t = []
for i in range(a):
  s.append(int(input()))
for i in range(b):
  t.append(int(input()))
s = [-1*inf] + s + [inf]
t = [-1*inf] + t + [inf]
for i in range(q):
  x = int(input())
  index_s = bisect.bisect_left(s, x)
  index_t = bisect.bisect_right(t, x)
  s1 = abs(s[index_s]-x)#xより右側で一番近い神社までの距離
  s2 = abs(s[index_s-1]-x)#xより左側で~
  t1 = abs(t[index_t]-x)#xより右側で~寺~
  t2 = abs(t[index_t-1]-x)#xより左側で~
  print(min([max(s1, t1), max(s2, t2), 2*s1+t2, 2*t2+s1, 2*s2+t1, 2*t1+s2]))