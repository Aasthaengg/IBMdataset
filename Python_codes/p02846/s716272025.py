def meet(faster, slower):
  if slower[0] - faster[0] < 0:
    print(0)
  else:
    count = (slower[0] - faster[0]) // (sum(faster) - sum(slower))
    if (slower[0] - faster[0]) % (sum(faster) - sum(slower)) == 0:
      print(count * 2)
    else:
      print(count * 2 + 1)

t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

at1 = a1 * t1
at2 = a2 * t2
bt1 = b1 * t1
bt2 = b2 * t2

if at1 + at2 < bt1 + bt2:
  faster = [bt1, bt2]
  slower = [at1, at2]
  meet(faster, slower)
elif at1 + at2 > bt1 + bt2:
  faster = [at1, at2]
  slower = [bt1, bt2]
  meet(faster, slower)
else:
  print('infinity')