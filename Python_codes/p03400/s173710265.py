n = int(input())
d,x = map(int,input().split())
a = [0]*n

for i in range(0,n):
  a[i] = int(input())
  
ans = 0
for i in range(n):
  day = 1
  j = 1
  while True:
    if day > d:
      break
    else:
      ans += 1
      day = j*a[i] + 1
      j += 1
      
print(ans+x)