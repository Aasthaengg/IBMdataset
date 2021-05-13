N = int(input())
A = list(map(int, input().split()))

total, large = 0,0

for i in A:
  
  if large > i:
    total += (large - i)
  
  if i > large: large = i
    
print(total)