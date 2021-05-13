p = str(input())
q = str(input())

count = 0

for i in range(len(p)):
  if p[i] != q[i]:
    count = count + 1
    
print(count)