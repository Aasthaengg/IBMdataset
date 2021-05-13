#解説参照
#構成が無理
#テストどうやってんだろ
n = int(input())
a = list(map(int, input().split( )))

a.sort()
from bisect import bisect_left

j = bisect_left(a,0)
if j==0:
    j+=1
elif j==n:
    j-=1
print(sum(a[j:])-sum(a[:j]))
for i in range(j,n-1):
    print(a[0],a[i])
    a[0]-=a[i]

for i in range(j):
    print(a[-1],a[i])
    a[-1]-=a[i]
