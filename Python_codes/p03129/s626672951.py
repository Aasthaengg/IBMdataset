def main():
  N, K = map(int, input().split())
  if N % 2 == 0:
    X = N / 2
    if X >= K:
      print('YES')
    else:
      print('NO')
  else:
    X = (N + 1)/2
    if X >= K:
      print('YES')
    else:
      print('NO')
main()