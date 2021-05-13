
from math import floor

def parse():
  return map(int, input().split(" "))

def main():
  A, B, N = parse()
  
  x = B - 1 if B - 1 <= N else N
  print(floor((A * x) / B) - A * floor(x / B))
  exit(0)

  limit_N = 5000000
  N = limit_N if N > limit_N else N

  x = 0
  max_val = floor((A * x) / B) - A * floor(x / B)

  for x in range(1, N + 1):
    val = floor((A * x) / B) - A * floor(x / B)
    if max_val < val:
      max_val = val

  print(max_val)


if __name__ == "__main__":
  main()