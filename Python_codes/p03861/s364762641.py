def resolve():
  a, b, x = map(int, input().split(" "))

  diff = b - a
  result = diff // x
  if not x - a%x + b%x >= x or a%x == 0 or b%x == 0:
    result += 1

  print(result)

if __name__ == "__main__":
  resolve()