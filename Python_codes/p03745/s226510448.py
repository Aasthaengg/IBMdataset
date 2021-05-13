N = int(input())
A = list(map(int,input().split()))

prev = A[0]
isUp = True
isDown = True

ans = 0
for a in A[1:]:
  if prev == a:
    pass
  elif prev < a:
    isDown = False
    if not isUp:
      isUp = True
      isDown = True
      ans += 1
  elif a < prev:
    isUp = False
    if not isDown:
      isUp = True
      isDown = True
      ans += 1
      
  prev = a
  
print(ans+1)

  
  
