def solve():
  r, d, x = map(int, input().split())
  for i in range(10):
    x = r*x-d
    print(x)
  return 0
 
if __name__ == "__main__":
  solve()
