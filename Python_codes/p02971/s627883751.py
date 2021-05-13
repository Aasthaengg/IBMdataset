n = int(input())
a = [int(input()) for _ in range(n)]
a_sort = sorted(a,reverse=True)
m1 = a_sort[0]
m2 = a_sort[1]
for i in range(n):
  if a[i] == m1:
    print(m2)
  else:
    print(m1)