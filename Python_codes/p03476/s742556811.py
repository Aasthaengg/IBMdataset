import bisect
N = 10**5
Q = int(input())
 
lst1 = set([2])
for L in range(3, N, 2):
    if all(L % L2 != 0 for L2 in lst1):
        lst1.add(L)

lst2 = [i for i in lst1 if (i+1)//2 in lst1]
 
lst2.sort()
 
for _ in range(Q):
  l, r = map(int, input().split())
  a = bisect.bisect_left(lst2, l)
  b = bisect.bisect_right(lst2, r)
  print(b-a)