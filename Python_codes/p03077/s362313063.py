def resolve():
  n = int(input())
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  e = int(input())

  x = min(a, b, c, d, e)
  ans = (n + x - 1) // x + 4
  print(ans)

  return

if __name__ == "__main__":
  resolve()
