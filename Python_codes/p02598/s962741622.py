N, K = map(int, input().split())
AList = list(map(int, input().split()))

l = 0
r = 10**9
while r-l > 1:
  x = (l + r)//2
  now = 0
  for a in AList:
    now += (a-1)//x
  f = lambda now : True if now <= K else False
  if f(now):
    r = x
  else:
    l = x
print(r)