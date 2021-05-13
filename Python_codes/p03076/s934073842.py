L = [int(input()) for i in range(5)]
l = []
for i in L:
  if i%10==0:
    l.append(0)
  else:
    l.append(10-i%10)
print(sum(L)+sum(l)-max(l))