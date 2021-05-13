from collections import Counter
n=int(input())
a=list(map(int,input().split()))
c=Counter(a).most_common()
s=[0,0]
for v in c:
  if v[1]>=2:
    for _ in range(v[1]//2):
      s.append(int(v[0]))
s.sort()
print(s[-1]*s[-2])
