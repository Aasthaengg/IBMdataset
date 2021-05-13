# AGC 011 B - Colorful Creatures
from itertools import accumulate
n=int(input())
a=list(map(int,input().split()))
a.sort()
b=[0]+a
b=list(accumulate(a))
# print('a:',a)
# print('b:',b)
cnt=0
for i in range(n-1):
    if a[i+1]>2*b[i]:
        cnt=i+1
print(n-cnt)