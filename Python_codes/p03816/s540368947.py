n = input()
n = int(n)
ss = input().split()
sslist = sorted(ss)
# print(sslist)
dic_ss = {}
for x in sslist:
  dic_ss.setdefault(x,0)
  dic_ss[x] += 1
# print(dic_ss)
# 1) 3回以上の重複があれば、その数字だけを使って、排除 N -> N-2
for key, value in dic_ss.items():
  while value >= 3:
    value -= 2
  dic_ss[key] = value
# print(dic_ss)
# 2) 2回重複の最小値と最大値を使って重複排除 Min N -> N-1, Max M -> M-1
key1 = None
key2 = None
for key, value in dic_ss.items():
  if key1 == None and value == 2:
    key1 = key
  elif key2 == None and value == 2:
    key2 = key
  if key1 != None and key2 != None:
    dic_ss[key1] = 1
    dic_ss[key2] = 1
    key1 = None
    key2 = None
# print(dic_ss)
# 3) 2回重複が1つ残ったら、重複なしから1つ削除
count = len(dic_ss)
for key, value in dic_ss.items():
  if value > 1:
    count -= 1
print(count)