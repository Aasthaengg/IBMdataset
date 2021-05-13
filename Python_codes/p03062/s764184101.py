#他の数字はそのままで，任意の2数の符号を同時に反転させることが可能．マイナスの数の偶奇で場合分け
n = int(input())
a = list(map(int,input().split()))
aabs = [i if i>=0 else i*(-1) for i in a]
MIN = min(aabs)
ans = 0
mcount = 0

for i in range(n):
  if a[i] < 0:
    mcount += 1
    
if mcount%2 == 0:
  for i in a:
    ans += abs(i)
  print(ans)
else:
  for i in a:
    ans += abs(i)
  print(ans - 2*MIN)