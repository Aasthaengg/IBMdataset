import copy
s=input()
check="keyence"
tmp=6
sNow=0
cNow=0
#一度目のチェック
for i in s:
  sNow+=1
  if i == check[cNow]:
    cNow+=1
  else:
    break
#最初に見つかれば終了
if cNow == 7:
  print("YES")
  exit()

#print(check[cNow:], s[-1*(7-cNow):])
"""
sの最後が"keyence"の残りの文字と一致すればOK
例：keyaence
最初の"key"は合っているので，残りは"aence"の内"a"を除いたもの
cNow=3, 7-cNow=4
後ろの４文字が"ence"ならばYESとなる
"""
if check[cNow:] == s[-1*(7-cNow):]:
  print("YES")
else:
  print("NO")