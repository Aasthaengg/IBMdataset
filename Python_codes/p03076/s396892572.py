A = []
m = 0
ans = 0
for i in range(5):
  a = int(input())
  if a%10 != 0:
    if round(a+5, -1) - a > m:
      m = round(a+5, -1) - a
    ans += round(a+5,-1)
  else:
    ans += a
print(ans-m)