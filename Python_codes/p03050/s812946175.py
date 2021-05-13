n = int(input())
ans=0

if n == 1:
  print(0)
  quit()

for i in range(1, n):
  #余り、商がiになるmを求める。mが整数で、余りより大きければ答えに加える。
  #iは単調増加、mは単調減少だから、mが余りより小さくなったら打ち切る。
  temp=n-i
  syou=temp/i
  if syou>i:
    if syou.is_integer():
      ans+=int(syou)
  else:
    break
print(ans)