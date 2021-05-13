n=int(input())
s=input()
x=0
m=-101
for i in s:
  if x>m:
    m=x
  if i=="I":
    x=x+1
  else:
    x=x-1
  if x>m:
    m=x
print(m)