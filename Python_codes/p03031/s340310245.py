import itertools

n, m = map(int, input().split())
switches = []
for i in range(m):
  switches.append(input())
lights = list(map(int, input().split()))

switch = [0, 1]
lists = list(itertools.product(switch, repeat=n))
count = 0
for l in lists:
  for i in range(m):
    on = 0
    switches_list = list(map(int, switches[i].split()))
    switch_num = lights[i]
    repeat_num = switches_list[0] + 1
    for j in range(1, repeat_num):
      switch_pos = switches_list[j] - 1
      on += l[switch_pos]
    if on % 2 != switch_num:
      break
    if i == m - 1:
      count += 1
print(count)