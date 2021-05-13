from collections import Counter

a = input()
a_list = list(map(int, input().split()))
 
# 要素数の数え上げと取り出し
num_counter = Counter(a_list)
num_keys = sorted(num_counter.keys(), reverse=True)

big = 0
small = 0

for i in num_keys:
  x = num_counter[i]
  if x >= 4:
    if big == 0:
      big = small = i
    elif big != 0 and small == 0:
      small = i
  elif x == 3 or x == 2:
    if big == 0:
      big = i
    elif big != 0 and small == 0:
      small = i
  if big != 0 and small != 0:
    break
print(big * small)