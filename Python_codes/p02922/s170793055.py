m, n = input().split()
m, n = int(m), int(n)
 
tot = 0
a = 1
while a<n:
  a-=1
  a+=m
  tot+=1
 
print(tot)