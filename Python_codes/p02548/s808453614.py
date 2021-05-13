n = int(input())

tot = 0

for a in range(1,n):
  tot = tot + (n-1) // a
  
print(tot)