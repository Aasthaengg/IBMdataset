a = list(map(int, input().split()))
x = a[:2]
y = a[2:]
num = []
for i in x:
  for j in y:
    num.append(i * j)
    
  
print(max(num))