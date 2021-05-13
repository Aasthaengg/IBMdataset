def div2_count(n):
  if n % 2 != 0: return 0
  else: return 1 + div2_count(n / 2)
 
N = int(input())
ans = 1
count = 0
 
for i in range(N, 1, -1):
  tmp = div2_count(i) 
  if tmp > count: 
    ans = i
    count = tmp
    
print(ans)