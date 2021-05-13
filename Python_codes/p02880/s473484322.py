n=int(input())
c=0
for i in range(9):
  if n%(i+1)==0 and n/(i+1)<10 :
    c=1
if c==1:
  print("Yes")
else:
  print('No')
