def main():
  N, A, B = map(int, input().split())

  ans = (A + B * (N - 1)) - (A * (N - 1) + B)

  if ans < 0:
    ans = 0
  else:
    ans += 1

  print(ans)

main()
