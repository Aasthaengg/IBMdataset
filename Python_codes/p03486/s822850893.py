s = str(input())
t = str(input())
S = [i for i in s]
S.sort()
T = [i for i in t]
T.sort(reverse=True)
s = ''.join(S)
t = ''.join(T)
if s < t:
  print('Yes')
else:
  print('No')