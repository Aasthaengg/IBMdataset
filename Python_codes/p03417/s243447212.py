def main():
  N, M = (int(_) for _ in input().split())
  if N > 1 and M > 1:
    N = max(0, N-2)
    M = max(0, M-2)
    print(N * M)
  else:
    if N * M == 1:
      print(1)
    else:
      print(max(max(N, M)-2, 0))
  return

if __name__ == '__main__':
  main()