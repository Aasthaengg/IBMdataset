from itertools import chain

def process(l, ans):
  if not l:
    return ans
  elif len(l) == 1:
    ans += l[0]
    return ans
  elif all(l):
    ans += min(l)
    l = list(map(lambda x: x - min(l), l))
    ans = process(l, ans)
  else:
    d = [i for i in range(len(l)) if not l[i]]
    tmp = []
    td = 0
    for i, dd in enumerate(d):
      tmp.append(l[td:dd])
      td = dd + 1
      if i == len(d) - 1 and dd != len(l) -1:
        tmp.append(l[td:])
    for t in tmp:
      ans = process(t, ans)
  return ans

N = int(input())
h = list(map(int, input().split()))

ans = 0
ans = process(h, ans)
  
print(ans)