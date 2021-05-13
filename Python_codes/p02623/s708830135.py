#k分たったときには机Aの本を上から何冊か、机Bの本を上から何冊か読んでることになる
#つまり机A,Bの方で読んだ本の合計時間は累積和で計算可能
#あとはその範囲内で全探索すればいい
#その際Aの読む数を決めておけばBの方は2分探索で決められる
n,m,k=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
from itertools import accumulate
a=[0]+list(accumulate(a))
b=[0]+list(accumulate(b))
from bisect import bisect_right
c=bisect_right(a,k)
ans=0
for i in range(c):
  ans=max(ans,i+bisect_right(b,k-a[i])-1)
  
  
print(ans)
