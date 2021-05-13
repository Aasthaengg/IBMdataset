R,G,B,N = map(int,input().split())
ans = 0

if R == 1 and G == 1:
  for b in range(N//B+1):
    ans += N-b*B+1

else:
  for r in range(N//R+1):
    for g in range(N//G+1):
      bB=N-r*R-g*G
      if bB >= 0 and bB%B == 0:
        ans += 1

print(ans)