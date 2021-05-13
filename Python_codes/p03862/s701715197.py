N, x = map(int, input().split())
As = list(map(int, input().split()))
As.append(0)

f = sum(As)
  
for i in range(0,N):
  if As[i]+As[i+1] > x:
    if As[i] <= x:
      As[i+1] = x - As[i]
    else:
      As[i+1] = 0
      As[i] = x

s = sum(As)

print(f-s)