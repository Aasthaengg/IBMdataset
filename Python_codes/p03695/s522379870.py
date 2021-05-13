def resolve():
  n = int(input())
  aa = list(map(int, input().split()))
  s = set()
  num = 0
  for a in aa:
    if a >= 3200:
      num += 1
    else:
      s.add(a // 400)
  print(max(len(s), 1), len(s) + num)
  return

if __name__ == "__main__":
  resolve()
