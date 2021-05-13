import math, collections
n, a, b = map(int, input().split())
list_v = [int(v) for v in input().split()]
list_v.sort(reverse=True)
list_ave = []
list_num = []
for i in range(a, b+1):
  temp_ave = sum(list_v[:i]) / len(list_v[:i])
  list_ave.append(temp_ave)
  list_num.append(i)
max_ave = max(list_ave)
print(max_ave)

list_target = [list_num[i] for i, v in enumerate(list_ave) if v == max_ave]
count = collections.Counter(list_v)
sort_count = sorted(count.items(), reverse=True)
res = 0
for one_num in list_target:
  r = one_num
  for o in sort_count:
    temp = r - o[1]
    if temp <= 0:
      res += math.factorial(o[1]) // (math.factorial(o[1]-r) * math.factorial(r))
      break
    else:
      r -= o[1]
print(res)