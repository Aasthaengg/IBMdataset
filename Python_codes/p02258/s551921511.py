n = int(raw_input())
max = -(10**9)
x1 = input() 
min = x1

for i in range(n-1):
 x = int(raw_input())

 if max < x-min:
  max = x- min
 if x< min:
  min = x
  
print max