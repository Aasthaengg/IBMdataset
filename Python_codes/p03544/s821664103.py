n = int(input())
l = [2, 1]
i = 0
while i < n:
  l.append(l[-1] + l[-2])
  i+=1
print(l[n])
