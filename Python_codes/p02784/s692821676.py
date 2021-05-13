MM = input().split()
H = int(MM[0])
N = int(MM[1])
AA = input().split()
total = 0
for i in AA:
  total += int(i)
if total >= H:
  print('Yes')
else:
  print('No')