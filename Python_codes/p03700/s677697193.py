import sys
input = sys.stdin.readline
n,a,b = map(int,input().split())
hls = [int(input()) for i in range(n)]
l = 0
r = sum(hls)
while l<r:
  x = (l+r)//2
  cnt = 0
  for hp in hls:
    if hp-x*b>0:
      cnt += (hp-x*b+(a-b)-1)//(a-b)
  if cnt>x:
    l = x+1
  elif cnt<x:
    r = x
  else:
    ans = x
    break
if l == r:
  ans = l
print(ans)