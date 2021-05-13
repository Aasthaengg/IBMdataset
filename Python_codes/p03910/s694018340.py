n = int(input())

s = 0
i = 0 
ans = []
# 値をカウントアップしていき、nを超える値になるまで繰り返す。
# 全ての値を保存する
while s < n:
  i += 1
  s += i
  ans.append(i)
  
delete = s - n # 取得した合計値からnを引き、差分を取得
if delete != 0: ans.remove(delete) # 差分を削除
  
for t in ans: print(t)