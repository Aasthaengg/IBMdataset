import itertools
import math
N = int(input())
ls = []
ans = 0
for i in range(N):
  x,y = map(int,input().split())
  ls.append([x,y])
ls2 = []
for i in itertools.permutations(ls,N):
  ls2.append(list(i))
for i in range(math.factorial(N)):
  ls3 = ls2[i]
  now_x = ls3[0][0]
  now_y = ls3[0][1]
  for j in range(1,N):
    ans += ((now_x - ls3[j][0])**2 + (now_y - ls3[j][1]) ** 2)**0.5
    now_x = ls3[j][0]
    now_y = ls3[j][1]
print(ans/math.factorial(N))