A,B = (int(x) for x in input().split())

time=A+B
if time < 24:
  print(time)
elif time >= 24:
  print(time - 24)
