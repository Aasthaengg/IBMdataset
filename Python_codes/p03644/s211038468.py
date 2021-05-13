n = int(input())
s=[]
for i in range(n+1):
  for j in range(n+1):
    if 2**j==i :
      s.append(i)

print(max(s))