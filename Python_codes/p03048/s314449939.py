R, G, B, N = map(int, input().split())
ans = 0

a = max(R, G, B)
if a == R:
  b = max(G, B)
elif a == G:
  b = max(B, R)
else:
  b = max(R, G)
c = min(R, G, B)
for i in range(N//a+1):
  for j in range((N-a*i)//b+1):
    if ((N-a*i)-b*j)%c == 0:
      ans += 1
print(ans)