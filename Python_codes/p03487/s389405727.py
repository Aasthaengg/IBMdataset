n = int(input())
L = list(map(int, input().split()))

count_num = dict()
for num in L:
  if num not in count_num:
    count_num[num] = 1
  else:
    count_num[num] += 1

removals = 0
for k, v in count_num.items():
  if k == v:
    continue
  elif k < v:
    removals += (v - k)
  else:
    removals += v

print(removals)
