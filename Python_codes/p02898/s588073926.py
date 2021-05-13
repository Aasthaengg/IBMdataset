# 数値の取得
people,hlimit = map(int,input().split())
height = list(map(int,input().split()))

# 条件に適合する人数をチェックし出力
check = []
for i in range(0,people,1):
  if height[i] >= hlimit:
    check.append("OK")
  else:
    check.append("NG")
hcnt = check.count("OK")
print(hcnt)