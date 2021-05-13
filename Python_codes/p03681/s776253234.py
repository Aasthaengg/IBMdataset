n,m = map(int, input().split())

if abs(n-m) >= 2:
  print(0)
  exit()

mod = 10**9+7
ans = 1
# 犬の組み合わせを取得
for i in range(1, n+1):
  ans *= i
  ans %= mod

# 犬の組み合わせに猿の組み合わせを入れる
for j in range(1, m+1):
  ans *= j
  ans %= mod

# 犬と猿が同数の場合は組み合わせが倍になる
# （例） 
# 同数の場合 ⚪⚫⚪⚫ or ⚫⚪⚫⚪
# 片方が多い場合 ⚪⚫⚪⚫⚪
if n == m:
  ans *= 2
  ans %= mod
  
print(ans)