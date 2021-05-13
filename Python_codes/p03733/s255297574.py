a,b = map(int,input().split())
ls = list(map(int, input().split()))

duration = 0 
max = 0

for i in ls :
  if  i <= max and max <= i+b :	
    duration += i + b - max  
    max = i + b
    
  elif max < i :
    duration += b
    max = i + b
    
print(duration)    