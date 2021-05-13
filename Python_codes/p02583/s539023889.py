n = int(input())
length = list(map(int,input().split()))

# n = 1 or 2
if n == 1 or n == 2:
  print(0)
  exit()

# n >= 3
len_count = {}
for l in length:
  if l not in len_count:
    len_count[l] = 1
  else:
    len_count[l] += 1

uniq_len = sorted(list(set(length)))
n_len = len(uniq_len)
triangle = []

from itertools import combinations
for c in combinations(uniq_len,3):
  c = sorted(list(c))
  if c[0] + c[1] > c[2]:
    triangle.append(c)
      
ans = 0
for t in triangle:
  ans += len_count[t[0]] * len_count[t[1]] * len_count[t[2]]

print(ans)