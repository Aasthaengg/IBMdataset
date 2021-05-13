a,b = map(int, input().split())
c = [1,3,5,7,8,10,12]
d = [4,6,9,11]
if a in c:
  if b in c:
    print('Yes')
  else:
    print('No')
elif a in d:
  if b in d:
    print('Yes')
  else:
    print('No')
else:
  print('No')