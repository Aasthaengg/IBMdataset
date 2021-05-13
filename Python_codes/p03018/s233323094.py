def resolve():
  s = input()
  s = s.replace('BC', 'D')
  s = s.replace('B', 'C')

  ans = 0
  count = 0
  for c in s:
    if c == 'C':
      count = 0
      continue
    if c == 'A':
      count += 1
    if c == 'D':
      ans += count

  print(ans)


if __name__ == "__main__":
  resolve()
