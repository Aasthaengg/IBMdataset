import collections

n=int(input())
a=list(map(int,input().split()))

c=collections.Counter(a)
s=0

for i in c.values():
  s+=i*(i-1)//2 #ボールを抜かない場合に2つのボールを選ぶ方法の数

for j in a:
  f=c[j]
  print(s-(f-1)) #下記メモ参照

'''
複数個のボールから1個のボールが抜かれる場合、i*(i-1)//2が(i-1)*(i-2)//2となる。

i*(i-1)//2-(i-1)*(i-2)//2
=i-1

よって、2つのボールを選ぶ方法が(i-1)だけ減る。
'''