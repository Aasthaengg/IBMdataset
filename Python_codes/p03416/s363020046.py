a,b = map(int,input().split())

c = 0
for i in range(a,b+1):
  a = str(i)
  if(a == a[::-1]):
    c = c + 1
print(c)