def resolve():
  x, t = map(int, input().split())
  print(max(x-t, 0))
  return

if __name__ == "__main__":
  resolve()
