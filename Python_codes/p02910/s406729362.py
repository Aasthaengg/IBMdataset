S =str(input())
S.split()

kisu = ['R', 'U', 'D']
gusu = ['L', 'U', 'D']
c = 0

for i in range(len(S)):
  if i%2 == 0:
    if S[i] in kisu:
      c += 1
  else:
    if S[i] in gusu:
      c += 1
      

if c == len(S):
  print('Yes')
else:
  print('No')
      
