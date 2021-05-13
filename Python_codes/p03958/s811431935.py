k, t = map(int, input().split())
a = [int(x) for x in input().split()]

if t == 1:
  ans = k-1
else:
  key = max(a)
  if key <= (k+1)//2:
    ans = 0
  else:
    ans = 2*key-k-1

print(ans)