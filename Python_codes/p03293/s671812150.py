S = input()
T = input()
s1 = S
while True:
  if s1 == T:
    print('Yes')
    exit()
  s1 = s1[-1]+s1[:-1]
  if s1 == S:
    print('No')
    exit()