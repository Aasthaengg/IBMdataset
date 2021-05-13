n= list(input())
for i in range(len(n)):
  n[i] = '1' if n[i]=='9' else '9'
print(''.join(n))