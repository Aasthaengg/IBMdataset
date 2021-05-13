def resolve():
  a, b, c, d = map(int, input().split())
  for i in range(100):
    c -= b
    if c <= 0:
      print('Yes')
      return
    a -= d
    if a <= 0:
      print('No')
      return
  return

if __name__ == "__main__":
  resolve()
