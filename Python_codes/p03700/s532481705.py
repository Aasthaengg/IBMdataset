import math
n, a, b = map(int, input().split())
list_enemy = [int(input()) for _ in range(n)]
list_enemy.sort(reverse=True)

diff_dam = a - b
min_a = math.ceil(list_enemy[-1] / a)
max_a = math.ceil(list_enemy[0] / b)
while max_a - min_a > 1:
  mid_a = min_a + (max_a - min_a) // 2
  count = 0
  for one_enemy in list_enemy:
    rest_h = one_enemy - (b * mid_a)
    if rest_h > 0:
      count += math.ceil(rest_h / diff_dam)
    else:
      break
  if count <= mid_a:
    max_a = mid_a
  else:
    min_a = mid_a
print(max_a)