import collections

N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

Dc = collections.Counter(D)
Tc = collections.Counter(T)

for Tkey,Tval in Tc.items():
    Dval = Dc[Tkey]
    if Dval < Tval:
        print('NO')
        exit()
print('YES')
