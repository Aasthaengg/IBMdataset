n = int(input())
l = []
for i in range(n):
  if (i+1)%3 != 0 and (i+1)%5 != 0:
    l.append(i+1)
  else:
    l.append(0)
print(sum(l))