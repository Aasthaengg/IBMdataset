import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

s = input()
n = len(s)
w = int(input())
ans = ""
for i in range(0,n,w):
  ans += s[i]
print(ans)