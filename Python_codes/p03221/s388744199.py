from bisect import bisect_left 
n,m = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(m)]
#print(l)
k = [[] for i in range(n)]
for j,h in l:
  k[j-1].append(h)
k_so = [[] for i in range(n)]
for i in range(n):
  a = k[i]
  k_so[i] = sorted(a)
#print(k_so)
for j,h in l:
  first = "{:0=6}".format(j)
  t = bisect_left(k_so[j-1], h)
  second = "{:0=6}".format(t+1)
  print(first+second)