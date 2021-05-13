def solve():
  N = int(input())
  lines = [input().split() for i in range(N)]
  count = 0
  for d,e in lines:
    if d==e:
      count += 1
      if count>=3:
        print("Yes")
        return
    else:
      count = 0
  print("No")
  return

solve()
