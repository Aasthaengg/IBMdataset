R, G, B, N = map(int, input().split())
counter = 0
r_max = N//R+1
for r in range(r_max+1):
  temp = N - R*r
  for g in range(temp//G+1):
    now = temp - G*g
    if now% B == 0 and now//B >= 0:
      counter +=1
print(counter)