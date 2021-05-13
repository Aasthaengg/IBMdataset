n = int(input())
s = list(input().split())

l = []
for i in s:
  if i not in l:
    l.append(i)
if len(l) == 3:
  print('Three') 
else:
  print('Four')