H = int(input())
count = 1
enemy = 1
while H>1:
  H = H//2
  enemy = enemy * 2
  count = count + enemy
print(count)