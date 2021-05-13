n = int(input())
rt = n
def sums(st: str):
  return sums(st[:-1])+int(st[-1]) if len(st) >1 else int(st)
for a in range(1,n//2):
  b = n - a
  tmp = sums(str(b)) + sums(str(a))
  if tmp < rt:
    rt = tmp
print(rt)