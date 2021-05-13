A,B = map(int, input().strip().split(' '))
for c in [A,B,A+B]:
  if c % 3 == 0:
    print('Possible')
    exit()
print('Impossible')
