n,q = map(int,input().split())
s = input()

li = [0]*n

for i in range(1,n):
    if s[i-1] == "A" and s[i] == "C":
        li[i] += 1

from itertools import accumulate

lin = [0]+list(accumulate(li))

for _ in range(q):
    l,r = map(int,input().split())
    print(lin[r]-lin[l])