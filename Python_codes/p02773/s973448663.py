n=int(input())
s=[str(input()) for _ in range(n)]
import collections
cnt=collections.Counter(s)
cntt=cnt.most_common()
maxn=cntt[0][1]
ansl=[]
for c in cntt:
  if c[1]==maxn:
    ansl.append(c[0])
  else:
    break
ansl.sort()
for i in ansl:
  print(i)