a,b,k = map(int, input().split())

l = []
for i in range(1,101):
  if a % i == b % i == 0:
    l.append(i)
    
l.sort()
print(l[(-1)*k])