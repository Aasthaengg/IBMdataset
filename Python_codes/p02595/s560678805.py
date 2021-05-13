n,d = input().split(" ")

count = 0
for i in range(int(n)):
  x,y = input().split(" ")
  
  r = (int(x)**2+int(y)**2)**(1/2)
  
  if r <= int(d):
    count += 1
print(count)