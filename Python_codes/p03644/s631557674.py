def div_by_two(n):
  if n % 2 == 1:
    return 0
  else:
    return div_by_two(n / 2) + 1
  
N = int(input())
count = 0
res = 1
for i in range(1, N+1):
  tmp = div_by_two(i)
  if tmp > count: 
    res = i
    count = tmp 

print(res)