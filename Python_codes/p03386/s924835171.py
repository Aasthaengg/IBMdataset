a, b, k = map(int, input().split())

used = set()
for i in range(a, min(a+k, b)):
  print(i)
  used.add(i)
for i in range(max(a, b-k+1), b+1):
  if not i in used:
    print(i)