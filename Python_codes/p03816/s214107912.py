n=int(input())
a=list(map(int,input().split()))

from collections import Counter

kaburi=0
c=Counter(a).most_common()
for i in c:
  if i[1]>=2:
    kaburi+=i[1]-1

if kaburi%2:
  w=n-kaburi-1
else:
  w=n-kaburi

print(w)