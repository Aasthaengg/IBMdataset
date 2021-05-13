x, y = map(int, input().split())

if x == 0 and y < 0:
  print(abs(y) + 1)

elif x < 0 and y == 0:
  print(abs(x))

elif x > 0 and y == 0:
  print(x+1)

elif x >= 0 or y >= 0:
  if x == y:
    print(0)

  elif x == -y:
    print(1)

  elif x > y:
    # (11, 7)
    if y >= 0:
      ans = 2
      ans += x - y
      print(ans)

    # (11, -7)
    else:
      print(1 + abs(abs(x) + y))

  else:
    # (7, 11)
    if x >= 0:
      print(y - x)

    # (-7, 11)
    else:
      print(1 + abs(abs(y) + x))

else:
  if x == y:
    print(0)


  else:
    if x > y:
      print(abs(y) - abs(x) + 2)
    else:
      print(abs(x) - abs(y))
