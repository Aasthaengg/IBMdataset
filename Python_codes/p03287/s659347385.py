import itertools
import collections

n, m = map(int, input().split())
a=list(map(int,input().split()))
b =[0]+ list(itertools.accumulate(a))
count=0
for i in range(n+1):
    b[i]=b[i]%m

b=collections.Counter(b)
b=b.most_common()

for i in range(len(b)):
    if b[i][1]>=2:
        count+=b[i][1]*(b[i][1]-1)//2
    else:
        break
print(count)