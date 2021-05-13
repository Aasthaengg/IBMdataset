def resolve():
  s = input()
  num_b = 0
  num_r = 0
  for c in s:
    if c == '0':
      num_r += 1
    else:
      num_b += 1
  print(min(num_b, num_r) * 2)
  return

if __name__ == "__main__":
  resolve()
