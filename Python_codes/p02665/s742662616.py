n=int(input())
l=list(map(int,input().split()))
g=[1]
for i in range(n):
  #葉となるノード以外のノードの最大個数を作っていく。
  #各深さの限界がgとなる。
  g+=[(g[-1]-l[i])*2]
a=0
t=0
#後ろノードから見ていく。
for i in range(n,-1,-1):
  #-1出力のための限界値
  if l[i]>g[i]:
    print(-1)
    break
  #計算する前のtは、前のノードの個数
  #最大個数より小さくなることはない。
  t=min(l[i]+t,g[i])
  #このtが各深さによるノードの個数となっている。
  a+=t
else:
  print(a)

