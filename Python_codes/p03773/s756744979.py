A, B = map(int, input().split()) 
sum = A + B
if sum >= 24:
  sum = sum - 24
print(sum)