import copy
import string

s = list(input())
ans = 0
if len(set(s)) == 1:
  print(0)
else:
  for k in string.ascii_lowercase:
    tmp = 0
    l = copy.deepcopy(s)
    while any(ss != k for ss in l):
      for i in range(len(l) - 1):
        if l[i + 1] == k:
          l[i] = k
      l.pop(-1)
      tmp += 1
    if ans:
      ans = min(ans, tmp)
    else:
      ans = tmp
  print(ans)