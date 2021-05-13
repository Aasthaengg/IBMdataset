def get_int_list():
  return list(map(int, input().split()))


d, t, s = get_int_list()
if t * s >= d:
  print("Yes")
else:
  print("No")