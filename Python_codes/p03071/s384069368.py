ary = list(map(lambda n : int(n) , input().split(" ")))

if ary[0] == ary[1]:
  print(ary[0] * 2)
else:
  print(max(ary) * 2 - 1)