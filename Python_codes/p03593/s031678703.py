n,m=map(int,input().split())
#n,mの偶奇で場合分け
#n,mがともに偶数の時は全部４の倍数個なきゃダメ
#n,mの片方のみ奇数の時は、例えばnが奇数の時は個数が偶数だが４の倍数でない組みがm//2組みまで許される
#n,mがともに奇数の時は個数が偶数だが４の倍数でない組みが(n+m)//2組み許され、ただ一つ奇数が必要
l=[]
for i in range(n):
  l.append(list(input()))
from collections import defaultdict
d=defaultdict(int)
for i in range(n):
  for j in range(m):
    d[l[i][j]]+=1
b=True
count2=0
count1=0
for i in d:
  if d[i]%4==0:
    pass
  elif d[i]%2==0:
    count2+=1
  else:
    if count1!=0:
      b=False
    else:
      count1=1
if not b:#奇数個あるのが２組以上
  print("No")
else:
  if n%2==0 and m%2==0:
    if count2>0 or count1>0:
      print("No")
    else:
      print("Yes")
  elif n%2==0 and m%2==1:
    if count1>0 or count2>n//2:
      print("No")
    else:
      print("Yes")
  elif n%2==1 and m%2==0:
    if count1>0 or count2>m//2:
      print("No")
    else:
      print("Yes")
  else:
    if (count1-1)%4==2:
      count2+=1
    if count2>(n+m-2)//2:
      print("No")
    else:
      print("Yes")