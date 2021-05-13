while True:
  H, W = map(int, input().split())
  if H == W == 0: break
  print(('#.'*(W//2) + '#'*(W%2) + '\n' +'.#'*(W//2) + '.'*(W%2) + '\n')*(H//2) +('#.'*(W//2) + '#'*(W%2) + '\n')*(H%2))