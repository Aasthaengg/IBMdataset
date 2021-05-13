x,n = map(int,input().split())
if n == 0:
  ans = x
else:
  p = [int(i.strip()) for i in input().split()]
  for i in range(n+1):
    ch_1 = x-i
    ch_2 = x+i
    if p.count(ch_1) == 0:
      ans = ch_1
      break
    elif p.count(ch_2) == 0:
      ans = ch_2
      break
print(ans)