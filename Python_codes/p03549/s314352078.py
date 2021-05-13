def main():
  N, M = (int(_) for _ in input().split())
  print((100 * N + 1800 * M) * pow(2, M))
  return

if __name__ == '__main__':
  main()