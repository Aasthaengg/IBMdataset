def check():
  S = list(input())
  T = list(input())
  S.sort()
  T.sort(reverse=True)
  if S>=T:
    return 'No'
  return 'Yes'
print(check())