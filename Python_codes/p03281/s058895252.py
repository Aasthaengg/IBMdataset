c = 0
for i in range(1, int(input())+1):
  if not i%2:
    continue
  if sum(not(i%j) for j in range(1, i+1))==8:
    c += 1
print(c)