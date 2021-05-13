from collections import Counter
def check():
  N = int(input())
  D = list(map(int, input().split()))
  M = int(input())
  T = list(map(int, input().split()))
  d = Counter(D)
  t = Counter(T)
  for k,v in t.items():
    if d[k]<v:
      return 'NO'
  return 'YES'
print(check())