N=int(input())
s=input()
b_count=0
r_count=0
for i in range(N):
  if s[i]=='R':
    r_count+=1
  elif s[i]=='B':
    b_count+=1
if r_count>b_count:
  print('Yes')
else:
  print('No')