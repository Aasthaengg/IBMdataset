a,b,k = map(int,input().split())
cnt = 0
while cnt < k:
  b += a//2
  a = a//2
  cnt += 1
  if cnt < k:
    a += b//2
    b = b//2
    cnt += 1
print(a,b)