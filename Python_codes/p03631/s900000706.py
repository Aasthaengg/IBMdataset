n = input()
count = 0
for i in range(len(n)//2):
  if n[i] == n[-1 -1*i]:
    count += 1
if count == len(n)//2:
  print('Yes')
else:
  print('No')