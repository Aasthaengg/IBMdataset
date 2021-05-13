n =[]

for _ in range(4):
  n += map(int, input().split())

num = 0
  
for i in range(n[0]+1):
  for j in range(n[1]+1):
    for k in range(n[2]+1):
      total = 50*k + 100*j + 500*i
      if total == n[3]:
        num += 1
        
print(num)