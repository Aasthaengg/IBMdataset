import decimal

N = int(input())
a = list(int(i) for i in input().split())

mean = sum(a)/N
min  = float('inf') 

min_id = 0

for i, ai in enumerate(a):
  diff = abs(ai-mean)
  if(diff < min):
    min = diff
    min_id = i
  
print(min_id)