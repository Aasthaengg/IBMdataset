n, q = map(int, input().split())
s = input()
lst = [0] * (n + 1)
reach = False
for i in range(n):
  if s[i] == 'A':
    reach = True
    lst[i + 1] = lst[i]
  else:
    if reach and s[i] == 'C':
      lst[i + 1] = lst[i] + 1
    else:
      lst[i + 1] = lst[i]
    reach = False
lst.pop(0)
#print(lst)
for i in range(q):
  l, r = map(int, input().split())
  print(lst[r - 1] - lst[l - 1])