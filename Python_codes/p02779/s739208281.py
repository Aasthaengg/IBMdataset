def distinct(a):
  d = {}
  for num in a:
    try: d[num] += 1
    except KeyError: d[num] = 1
  for key in d:
    if d[key] > 1: return False
  return True
n = int(input())
a = list(map(int, input().split()))
print('YES' if distinct(a) else 'NO')