s= input()
k = sorted(s)
S = ''
for i in k:
  S += i
if S == 'abc':
    print('Yes')
else:
    print('No')