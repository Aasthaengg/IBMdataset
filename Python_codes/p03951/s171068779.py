n = int(input())
s = list(input())
t = list(input())

if s == t:
  print(n)
else:
  ans = n
  for i in range(n):
      if s[i:] == t[: - i]:
          print(ans)
          break
      else:
          ans += 1
  else:
      print(ans)
