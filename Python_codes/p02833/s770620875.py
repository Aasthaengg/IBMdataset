def resolve():
  N = int(input())

  if N%2:
    print(0)
    return True
  multiplier = 10
  result = 0
  while multiplier <= N:
    result += N // multiplier
    multiplier *= 5

  print(result)

if __name__ == "__main__":
  resolve()
