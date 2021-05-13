import sys
from collections import Counter
input = sys.stdin.readline
h,w,*a = map(int,input().split())
a = []
for i in range(h):
  a += list(input().strip())
m1 = (h%2)*(w%2)
m2 = (h%2)*(w//2)+(h//2)*(w%2)
c = Counter(a)
c1,c2, = 0,0
for i in c.values():
  dc2,dc1 = divmod(i%4,2)
  c1 += dc1
  c2 += dc2
print("Yes" if m1>=c1 and m2>=c2 else "No")