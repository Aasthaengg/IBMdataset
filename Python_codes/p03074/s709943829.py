from itertools import*
n, k = map(int, input().split())
s = input()
d = [len(list(t)) for _, t in groupby(s)]
if s[0] == "0":
    d = [0] + d
a = [0] + list(accumulate(d))
m = l = 0
while True:
  try:
    m = max(m, a[l+2*k+1] - a[l])
    l += 2
  except IndexError:
    m = max(m, a[-1] - a[l])
    break
print(m)