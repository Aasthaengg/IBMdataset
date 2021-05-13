S=str(input())
l=len(S)
key='keyence'
if S=='keyence':
  print('YES')
  exit()
else:  
  for i in range(1,l):
    for j in range(l):
      if S[0:j]+S[i+j:l]==key:
        print('YES')
        exit()
print('NO')