import bisect, math
N = 10**5
Q = int(input())

lst1 = [2]
for L in range(3, N, 2):
  f = 0
  for d in range(3, math.floor(math.sqrt(L))+1, 2):
    if L % d == 0:
      f = 1
      break
  if f == 0:
    lst1.append(L)

lst1 = set(lst1) 
lst2 = [i for i in lst1 if (i+1)//2 in lst1]

lst2.sort()

for _ in range(Q):
  l, r = map(int, input().split())
  a = bisect.bisect_left(lst2, l)
  b = bisect.bisect_right(lst2, r)
  print(b-a)