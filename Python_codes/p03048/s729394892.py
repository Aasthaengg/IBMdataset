R, G, B, N = map(int, input().split())
ans = 0
for i in range(N//R + 1):
  r = N - R*i
  for j in range(r//G + 1):
    if not (r - G*j) % B:
      ans += 1
      
print(ans)