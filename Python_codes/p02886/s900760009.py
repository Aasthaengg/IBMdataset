from itertools import accumulate as Z
n = input()
d = list(map(int,input().split()))
print(sum(a*b for a,b in zip(d[1:],Z(d))))