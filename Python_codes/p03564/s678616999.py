def resolve():
  n = int(input())
  k = int(input())
  ans = 1
  for i in range(n):
    if ans * 2 < ans + k:
      ans *= 2
    else:
      ans += k
  print(ans)
  return

if __name__ == "__main__":
  resolve()
