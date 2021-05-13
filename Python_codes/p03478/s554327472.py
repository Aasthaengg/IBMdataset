N, A, B = map(int, input().split())

# 別解：10で割った余りを足していく
ans = 0
for n in range(1, N+1):
  s = 0
  m = n
  while m > 0:
    s += m % 10
    m = m // 10
  if A <= s and s <= B: ans += n
    
print(ans)