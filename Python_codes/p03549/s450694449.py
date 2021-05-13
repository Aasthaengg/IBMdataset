def resolve():
  n, m = map(int, input().split())
  t = m * 1900 + (n-m) * 100
  print(t * pow(2, m))
  return

if __name__ == "__main__":
  resolve()
