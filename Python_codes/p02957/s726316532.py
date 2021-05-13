def resolve():
  a, b = map(int, input().split())
  if a > b:
    a, b = b, a
  ans = (b + a) // 2
  if abs(a-ans) == abs(b-ans):
    print(ans)
  else:
    print("IMPOSSIBLE")
  return

if __name__ == "__main__":
  resolve()
