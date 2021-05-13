N = int(input())
s = [int(input()) for _ in range(N)]

s.sort()
ans = sum(s)
if ans%10 != 0:
  print(ans)
else:
  for si in s:
    if si%10 != 0:
      print(ans-si)
      break
  else:
    print(0)