ans = 0
R, G, B, N = map(int, input().split())
rl = (N+R-1)//R+1
gl = (N+G-1)//G+1
bl = (N+B-1)//B
for r in range(rl):
  for g in range(gl):
    tmp = N - (r*R) - (g*G)
    if tmp < 0:
      break
    if tmp == 0:
      ans += 1
    elif tmp%B == 0 and tmp%B <= bl:
      ans += 1
print(ans)