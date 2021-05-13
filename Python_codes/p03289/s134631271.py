S = input()
n =len(S)
s = S.lower()


if S[0] != 'A':
  print('WA')
  exit()
else:
  for i in range(2, n-1):
    if S[i] != 'C':
      if S[i] != s[i]:
        print('WA')
        exit()
      
if S[n-1] != s[n-1] or S[1] != s[1]:
  print('WA')
  exit()
  
if S.count('C') != 1:
  print('WA')
  exit()
  
print('AC')