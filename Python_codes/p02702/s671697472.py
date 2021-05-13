S = input()[::-1]

#aのMOD求めるンゴ
MOD=2019
ls_rem_a=[]
d=1
for i in range(len(S)):
  ls_rem_a.append(int(S[i])*d%MOD)
  d = d*10%MOD

#次に累積和求めるンゴ
ls_rem_s=[0]
sum=0
for i in range(len(S)):
  sum+=ls_rem_a[i]
  sum%=MOD
  ls_rem_s.append(sum)

#最後にMODが同じやつの個数を調べるンゴ
from collections import Counter
C_rem = Counter(ls_rem_s)
ans=0
for i in C_rem.keys():
  n=C_rem[i]
  ans+=n*(n-1)//2
print(ans)