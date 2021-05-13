ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

import statistics as st

n = ii()
a = []
b = []
for i in range(n):
    aa,bb = mi()
    a.append(aa)
    b.append(bb)

a.sort()
b.sort()

minmed = st.median(a)
maxmed = st.median(b)

if len(a) %2 == 0:
    ans = maxmed*2 - minmed*2 + 1
else:
    ans = maxmed-minmed+1
print(int(ans) )