def mod10(n):
  ret = n if n%10 != 0 else 0
  return ret

n = int(input())
s = [int(input()) for _ in range(n)]
ssum = sum(s)
if ssum%10 != 0:
  print(ssum)
else:
  sdiv = list(map(mod10,s))
  if sdiv == [0]*n:
    print(0)
  else:
    sdiv = [i for i in sdiv if i!=0]
    print(ssum-min(sdiv))