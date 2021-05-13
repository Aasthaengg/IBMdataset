n=int(input())
l=[]
for i in range(int(n**0.5)+1):
  l.append(i**2)
print(max(l))
