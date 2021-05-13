S=input()
a=0
b=0
c=0
for i in range(len(S)):
  if S[i]=='a':
    a+=1
  elif S[i]=='b':
    b+=1
  else:
    c+=1
# print(a,b,c)
if abs(a-b)<=1 and abs(b-c)<=1 and abs(c-a)<=1:
  print('YES')
else:
  print('NO')