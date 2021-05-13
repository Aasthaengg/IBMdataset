N = int(input())
a_list = list(map(int, input().split()))

count = 1
up_flag = None
prev_a = a_list[0]
for a in a_list[1:]:
  if up_flag is None:
    if prev_a == a:
      continue
    up_flag = a > prev_a
  if up_flag and a >= prev_a:
    prev_a = a
    continue
  elif not up_flag and a <= prev_a:
    prev_a = a
    continue
  else:
    up_flag = None
    count += 1
    prev_a = a

print(count)