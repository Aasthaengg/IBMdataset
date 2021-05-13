S = input()
N = len(S)
s_set = set(S)
if len(s_set) == 1:
  print(0)
  quit()

ans = 100

def change_to_s(s):
  flag = True
  T = S
  while flag:
    _T = ''
    flag = False
    for i in range(len(T)-1):
      if s in [T[i], T[i+1]]:
        _T += s
      else:
        _T += T[i]
        flag = True
    T = _T
  return N - len(_T), _T

for s in s_set:
  n, t = change_to_s(s)
  ans = min(ans, n)

print(ans)