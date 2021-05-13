a,b = map(int,input().split())

num = 0
while True:
  if a * num - (num-1) >= b:
    break
    
  num += 1
  
print(num)