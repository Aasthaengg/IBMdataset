X = str(input())

# 文字列を4つのintに分裂
# 二分検索でヒットしたらタス、そうでなければ引く、listに履歴を残しておく

for i in range(2**3):
  ans = int(X[0])
  list = []
  for j in range(3):
    if (i>>j & 1) == 1:
      ans += int(X[j+1])
      list.append("+")
    else:
      ans -= int(X[j+1])
      list.append("-")
  if ans == 7:
    break

ans = X[0]
for i in range(3):
  ans += list[i]
  ans += X[i+1]
print(ans+"=7")