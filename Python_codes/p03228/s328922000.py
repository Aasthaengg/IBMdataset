a,b,k = map(int,input().split())
bit = 0
while k:
  if bit==0:
    if a%2!=0:
      a -= 1
    b += a//2
    a //= 2
    bit = 1
  else:
    if b%2!=0:
      b -= 1
    a += b//2
    b //= 2
    bit = 0
  k -= 1


print(a,b)