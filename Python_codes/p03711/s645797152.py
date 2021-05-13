x, y = map(int, input().split())
def grp(z):
  if z in [1,3,5,7,8,10,12]:
    return 'a'
  elif z in [4,6,9,11]:
    return 'b'
  elif z == 2:
    return 'c'
print('Yes' if grp(x) == grp(y) else 'No')