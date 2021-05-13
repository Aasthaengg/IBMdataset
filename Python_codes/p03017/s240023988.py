def resolve():
  n, a, b, c, d = map(int, input().split())
  a -= 1
  b -= 1
  c -= 1
  d -= 1
  s = input()

  # a と c の間に ## があったらだめ
  for i in range(a, c):
    if s[i] == '#' and s[i+1] == '#':
      print('No')
      return
  # b と d の間に ## があったらだめ
  for i in range(b, d):
    if s[i] == '#' and s[i+1] == '#':
      print('No')
      return
  # a が b を飛び越えないと行けない場合  b - d の間に ... がないとだめ
  if b < c and d < c:
    flag = False
    for i in range(b-1, d):
      if s[i] == '.' and s[i+1] == '.' and s[i+2] == '.':
        flag = True
    if not flag:
      print('No')
      return
  print('Yes')

  return

if __name__ == "__main__":
  resolve()
