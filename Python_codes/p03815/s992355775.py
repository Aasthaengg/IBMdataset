x = int(input())
#2回で3~11を作れる
count = 0
if x == 7:
  count=2
  x = 0
count += (x//11)*2
x = x%11
if x==0:
  count += 0
elif x>6:
  count+=2
else:
  count += 1
print(count)