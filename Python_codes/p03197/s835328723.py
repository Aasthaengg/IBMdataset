n=int(input())
x='second'
for i in range(n):
  a=int(input())
  if a%2==1:
    x='first'
    break
print(x)