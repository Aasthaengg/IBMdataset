N = int(input())
s = [int(input()) for _ in range(N)]
s = sorted(s)
if sum(s) % 10 != 0:
  print(sum(s))
  exit()
else:
  for i in range(N):
    if (sum(s) - s[i]) % 10 != 0:
      print((sum(s) - s[i]))
      exit()

print(0)