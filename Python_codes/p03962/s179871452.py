a, b, c = map(int, input().split())

if a != b and a != c and b != c:
  print('3')
elif a == b and b == c and c == a:
  print('1')
else:
  print('2')