N = int(input())
s = input()
t = input()

if s == t:
  print(N)
else:
  for i in range(1, N):
    if s[i:] == t[:-i]:
      print(N + i)
      exit()
  print(N * 2)