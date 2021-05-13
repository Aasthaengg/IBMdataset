N = int(input())
s = [int(input()) for _ in range(N)]

if sum(s) % 10:
  print(sum(s))
else:
  s2 = [i for i in s if i % 10]
  if s2:
    print(sum(s) - min(s2))
  else:
    print(0)