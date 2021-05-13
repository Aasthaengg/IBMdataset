N=int(input())
a='No'
for i in range(14):
  if N<0:
    break
  if N%4==0:
    a='Yes'
    break
  N-=7
print(a)