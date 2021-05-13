n,x = map(int,input().split())
a = [int(x.strip()) for x in input().split()]
a_sorted = sorted(a)
ch,ans = 0,0
for i in range(n):
  ch = sum(a_sorted[:i+1])
  if ch < x:
    ans += 1
  elif ch == x:
    ans += 1
    break
  else:
    break
if n == ans and sum(a) < x:
  ans -= 1
print(ans)