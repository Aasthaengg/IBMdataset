N = int(input())
ans = 0.0
for i in range(N):
  A,B = input().split()
  if B == "BTC":
    ans += 380000.0 * float(A)
  else:
    ans += float(A)
print(ans)