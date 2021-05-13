n = int(input())
march =[]

for i in range(n):
    a = input()
    ai = a[0]
    march.append(ai)

import collections
c = collections.Counter(march)

mm = c["M"]
aa = c["A"]
rr = c["R"]
cc = c["C"]
hh = c["H"]

import itertools
seq = [mm,aa,rr,cc,hh]
mmm = list(itertools.combinations(seq,3))

res= 0
for i in range(10):
    aaa = mmm[i]
    res += aaa[0]*aaa[1]*aaa[2]

print(res)