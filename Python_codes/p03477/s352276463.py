def resolve():
  a, b, c, d = map(int, input().split())
  l = a + b
  r = c + d
  if l > r:
    print("Left")
  elif r > l:
    print("Right")
  else:
    print("Balanced")
  return

if __name__ == "__main__":
  resolve()
