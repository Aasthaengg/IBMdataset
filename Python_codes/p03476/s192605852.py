# 下記ページを参考に実装している
# https://qiita.com/drken/items/56a6b68edef8fc605821#%E5%95%8F%E9%A1%8C-2-atcoder-abc-084-d---2017-like-number

# エラトステネスのふるいで最大値までの素数をO(1)で判別できるようにする

MAX = 10 ** 5 + 10
is_prime = [True] * MAX
is_prime[0] = False
is_prime[1] = False
for i in range(2, MAX):
  if not is_prime[i]:
    continue
  for j in range(i*2, MAX, i):
    is_prime[j] = False

# 2017と似た数字かどうか
like2017 = [0] * MAX
for i in range(2, MAX):
  if is_prime[i] and is_prime[(i+1)//2]:
    like2017[i] = 1

# 累積和
s = [0] * (MAX+1)
for i in range(MAX):
  s[i+1] = s[i] + like2017[i]
#print(is_prime[:10])
#print(like2017[:10])
#print(s[:10])

# クエリ処理
q = int(input())
for i in range(q):
  l, r = map(int, input().split())
  print(s[r+1] - s[l])