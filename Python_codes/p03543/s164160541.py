N = input()
n = []
for i in N:
  n.append(int(i))
if n[0] == n[1] == n[2] == n[3]:
  print('Yes')
elif n[0]==n[1]==n[2] or n[1]==n[2]==n[3]:
  print('Yes')
else:
  print('No')