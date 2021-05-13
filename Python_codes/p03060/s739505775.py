n = input()
v = input().split()
c = input().split()
sum = 0
for v1 , c1 in zip(v , c):
  if int(v1) - int(c1) > 0:
    sum += int(v1) - int(c1)
print(sum)
