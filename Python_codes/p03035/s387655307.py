def solve():
  a, b = map(int, input().split())
  if a >= 13:
    print(b)
  elif 13 > a >= 6:
    print(b//2)
  else:
    print(0)
  return 0
 
if __name__ == "__main__":
  solve()
