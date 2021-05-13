n = int(input())
tot = 1
divisor = 10**9 + 7
for i in range(2,n+1):
  tot = (tot*i) % divisor
  
print(tot)