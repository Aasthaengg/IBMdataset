n = int(input())

lst = set()
for _ in range(n):
  j = input()
  if j not in lst:
    lst.add(j)
print(len(lst))