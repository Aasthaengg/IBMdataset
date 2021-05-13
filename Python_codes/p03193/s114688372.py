def solve():
  n,h,w = (int(i) for i in input().split())
  ct = 0
  for i in range(n):
    a,b = (int(i) for i in input().split())
    if a>=h and b >= w:
      ct += 1
  print(ct)
solve()