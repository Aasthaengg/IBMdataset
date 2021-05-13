n = int(input())
p = []
for i in range(n):
  price = int(input())
  p.append(price)

p.sort(reverse = True)  
p[0] = p[0]//2
  
print(sum(p))