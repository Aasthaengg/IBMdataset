n, m = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))
d = {}  # key=match, val=num
d[2] = [1]
d[3] = [7]
d[4] = [4]
d[5] = [5, 3, 2]
d[6] = [9, 6]
d[7] = [8]
enable = [False] * 10
for a in l:
  enable[a] = True
memo = {}
# マッチをk(=2..7)本使う場合の一番大きい値を総当たり
def f(nokori, current):
  k = (nokori, current)
  if k in memo:
    return memo[k]
  if nokori <= 0:
    return current if nokori == 0 else -1
  temps = []
  for key, nums in list(d.items())[::-1]:
    for num in nums:
      if enable[num]:
        if nokori-key != 0 and current % 10 != 0 and current % 10 < num:
          # 98 ok, 89 重複するので最後の桁以外は skip
          continue
        temps.append(f(nokori-key, current*10+num))
        break
  memo[k] = max(temps)
  return memo[k]

# 余裕があるうちは一番マッチの本数が少ないモノをヤケクソで詰めまくる
hoge = False
for key, nums in list(d.items()):
    # print(key, nums, type(nums))
    for num in nums:
      if enable[num]:
        hoge = True
        break
    if hoge:
      break
cs = []
while n > 50:
  n -= key
  cs.append(str(num))

# ヤケクソで詰めたやつと総当たりで調べたマックスを並び替えて辞書順で大きくする
num_ans = str(f(n, 0))
print(''.join(sorted(list(num_ans) + cs)[::-1]))