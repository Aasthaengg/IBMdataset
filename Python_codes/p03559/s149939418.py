import bisect
N=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
total = 0
for i in range(N):
  total += bisect.bisect_left(a,b[i]) * (N - bisect.bisect_right(c,b[i]))
print(total)