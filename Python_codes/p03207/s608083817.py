n=int(input())
m=0
s=0
for i in range(n):
  a=int(input())
  s+=a
  if a >m:
    m=a 
d=m/2
print(int(s-d))