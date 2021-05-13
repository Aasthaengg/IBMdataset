def main():
  a, b = list(map(int, input().split()))
  if a < b:
    a, b = b, a
  while b > 1:
    r = a % b
    if r == 0:
      break
    a, b = b, r

  print(b)

  return 0


if __name__ == '__main__':
  main()