n=int(input())
lst = []
s = input().split(" ")
for i in range(n):
  if s[i] not in lst:
    lst.append(s[i])
if len(lst) == 3:
  print("Three")
else:
  print("Four")