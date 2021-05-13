x = list(map(int, input().split()))
l = []
for i in range(1, 101):
  if (x[0]%i) == 0 and (x[1]%i) == 0:
    l.append(i)
l.sort(reverse=True)
print(l[x[2]-1])