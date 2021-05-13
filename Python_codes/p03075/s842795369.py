l=[int(input()) for i in range(5)]
k=int(input())

import itertools

d=[]

for v in itertools.combinations(l,2):
    d.append(abs(v[0]-v[1]))

if max(d)>k:
    print(":(")
else:
    print("Yay!")
