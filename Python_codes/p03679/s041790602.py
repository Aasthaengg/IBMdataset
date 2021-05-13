def check():
  X, A, B = map(int, input().split())
  if A>=B:
    return 'delicious'
  if B-A>X:
    return 'dangerous'
  return 'safe'
print(check())