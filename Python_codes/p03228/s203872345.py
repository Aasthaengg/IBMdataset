a,b,k = map(int,input().split())
i = 0
while i < k:
  if a%2 == 1:
    a -= 1 
  a = a//2
  b += a
    
  if k-i == 1:
    break
  if b%2 == 1:
    b -= 1 
  b = b//2
  a += b
  i += 2
print(a,b)