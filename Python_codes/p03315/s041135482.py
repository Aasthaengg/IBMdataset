def resolve():
  s = input()
  ans = 0
  for c in s:
    if c == '+':
      ans += 1
    else:
      ans -= 1

  print(ans)

  return

if __name__ == "__main__":
  resolve()
