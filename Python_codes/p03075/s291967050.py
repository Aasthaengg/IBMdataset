li = []
for _ in range(5):
  a = int(input())
  li.append(a)
li.sort()
k = int(input())
if li[-1]-li[0] <= k:
  print('Yay!')
else:
  print(':(')