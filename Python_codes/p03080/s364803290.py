n = input()
s = input()
count = 0
for c in s:
  if(c == 'R'):
    count += 1
  else:
    count -= 1
if(count > 0):
  print("Yes")
else:
  print("No")