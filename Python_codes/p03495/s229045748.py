from collections import Counter

N,K=list(map(int, input().split()))
A=list(map(int, input().split()))

dic = dict(Counter(A))
ls = list(dic.items())
ls.sort(key=lambda x: x[1])

i=0
ans=0
res=len(ls)
while 1:
  if res <= K or i >= N:
    break
  ans += ls[i][1]
  i+=1
  res-=1
print(ans)