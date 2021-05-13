N = int(input())
ans = 0
q = 1
while(q ** 2 + q < N):
  m = (N - q) / q
  if(m.is_integer()):
    ans += int(m)
  q += 1
print(ans)