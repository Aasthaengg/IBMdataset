n = int(input())
lst = []
for i in range(n):
  s, p = input().split()
  p = int(p)
  lst.append((s, p, i+1))
lst_sorted = sorted(lst, key=lambda x: (x[0], -x[1], x[2]))
for _, _, num in lst_sorted:
  print(num)
