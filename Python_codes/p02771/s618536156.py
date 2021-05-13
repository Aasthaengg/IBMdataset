a,b,c = map(int,input().split())
if a == b:
  if a != c and b !=c:
    print('Yes')
  else:
    print('No')
elif a == c:
  if a != b and c != b:
    print('Yes')
  else:
    print('No')
elif b == c:
  if b != a and c != a:
    print('Yes')
  else:
    print('No')
elif a == b == c:
  print('No')
else:
  print('No')