import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
A = list(map(int,input().split()))
# + - + - のパターン
ans1 = 0
acum = 0
for i in range(n):
  pre_plus = i % 2 == 0
  acum += A[i]
  if (pre_plus and acum < 0) or (not pre_plus and acum > 0):pass
  elif not pre_plus:
    ans1 += 1-acum
    acum = 1
  else:
    ans1 += abs(acum-(-1))
    acum = -1
  # print(i,acum,ans1)

# + - + - のパターンnogyaku
ans2 = 0
pre_plus = 1
acum = 0
for i in range(n):
  pre_plus= i % 2 == 1
  acum += A[i]
  if (pre_plus and acum < 0) or (not pre_plus and acum > 0):pass
  elif not pre_plus:
    ans2 += 1-acum
    acum = 1
  else:
    ans2 += abs(acum-(-1))
    acum = -1

print(min(ans1,ans2))
# print(ans1,ans2)
