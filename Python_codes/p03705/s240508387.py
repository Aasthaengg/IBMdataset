def main():
  N, A, B = map(int, input().split())

  if N == 1:
    if A != B:
      ans = 0
    else:
      ans = 1
  else:
    if A > B:
      ans = 0
    elif A == B:
      ans = 1
    else:
      ans = (A + (N - 1) * B) - (A * (N - 1) + B) + 1

  print(ans)

main()
