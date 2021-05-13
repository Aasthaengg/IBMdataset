def resolve():
  h, w = map(int, input().split())
  s = []
  for i in range(h):
    s.append(input())

  for i in range(h):
    for j in range(w):
      if s[i][j] == '.':
        continue
      flag = False
      if i > 0 and s[i-1][j] == '#':
        flag = True
      if i < h-1 and s[i+1][j] == '#':
        flag = True
      if j > 0 and s[i][j-1] == '#':
        flag = True
      if j < w-1 and s[i][j+1] == '#':
        flag = True
      if not flag:
        print('No')
        return
  print('Yes')
  return

if __name__ == "__main__":
  resolve()
