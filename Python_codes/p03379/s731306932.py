n = int(input())
if n == 2:
  a, b = map(str,input().split())
  print(b + " " + a)
else:
  L = list(map(int, input().split()))
  M = sorted(L)
  c = (n + 1) // 2 - 1
  a = M[c + 1]
  b = M[c]
  for l in L:
    if l> b:
      print(b)
    else:
      print(a)