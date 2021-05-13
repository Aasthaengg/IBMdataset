n = int(input())
a = [int(i) for i in input().split()]
q = 0
for i in range(n):
 for j in range(i, n):
  t = a[i]
  a[i] = a[j]
  a[j] = t
  f = 1  
  lst = - 1100
  for k in a:
   f &= k > lst
   lst = k
  q |= f
  t = a[i]
  a[i] = a[j]
  a[j] = t
print("YES" if q else "NO")
