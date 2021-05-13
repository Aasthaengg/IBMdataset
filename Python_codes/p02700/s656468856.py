taka_l, taka_a, ao_l, ao_a = map(int, input().split())
con = 0

while True:
  if con % 2 == 0:
    ao_l -= taka_a
    if ao_l <= 0:
      print("Yes")
      break
    con += 1
  if con % 2 != 0:
    taka_l -= ao_a
    if taka_l <= 0:
      print("No")
      break
    con += 1

