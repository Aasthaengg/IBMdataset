def main():
  N, M = (int(_) for _ in input().split())
  ret = min(M // 2, N)
  M = M - 2 * ret
  ret += M // 4
  print(ret)

if __name__ == '__main__':
  main()