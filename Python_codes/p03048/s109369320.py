R, G, B, N = map(int, input().split())
l = [R, G, B]
l.sort(reverse=True)

ans = 0
for i in range(N//l[0]+1):
  mod = N - l[0]*i
  for j in range(mod//l[1]+1):
    n = mod - l[1]*j
    if n % l[2] == 0:
      ans += 1
print(ans)