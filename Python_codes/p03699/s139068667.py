n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))
lst.sort()
ac = sum(lst)
if ac % 10 != 0:
  print(ac)
  exit()
for i in range(n):
  if lst[i] % 10 != 0:
    print(ac - lst[i])
    exit()
print(0)