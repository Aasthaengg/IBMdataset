def process(H, W) : 
  str = '#' * (W + 2)
  print(str)
  for i in range(H) : 
    s = '#'
    s += input()
    s += '#'
    print(s)
  print(str)


H, W = tuple(map(int, input().split()))
process(H, W)
