L = [str(i) for i in range(1, int(input())+1)]
t = 0
for l in L:
  if len(l)%2!=0:
    t += 1
print(t)