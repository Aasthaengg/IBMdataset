n = int(input())
c=[]
for i in range(n+1):
  a = i**2
  if a <= n:
    c.append(a)
  else:
    break
print(max(c))