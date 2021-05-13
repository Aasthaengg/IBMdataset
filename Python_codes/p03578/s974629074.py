import collections
import sys

n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))

ct=collections.Counter(t)
cd=collections.Counter(d)
cct=list(ct.items())
#print(cc)
if n < m:
    print('NO')
else:
    for i in range(len(cct)):
        if cd[cct[i][0]]<cct[i][1]:
            print('NO')
            sys.exit()
    print('YES')