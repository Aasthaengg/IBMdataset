import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

A,B,Q = LI()
inf = 10**12
s = [-inf]+[I() for _ in range(A)]+[inf]
t = [-inf]+[I() for _ in range(B)]+[inf]
x = [I() for _ in range(Q)]

from bisect import bisect

# xiより東にある神社・寺の中で最も西にあるもの、xiより西にある神社・寺の中で最も東にあるものだけがあると思えばよい

for i in range(Q):
    y = x[i]
    a = bisect(s,y)
    b = bisect(t,y)
    s1,s2,t1,t2 = s[a-1],s[a],t[b-1],t[b]
    z1 = abs(y-s1)+abs(s1-t1)
    z2 = abs(y-s1)+abs(s1-t2)
    z3 = abs(y-s2)+abs(s2-t1)
    z4 = abs(y-s2)+abs(s2-t2)
    z5 = abs(y-t1)+abs(t1-s1)
    z6 = abs(y-t1)+abs(t1-s2)
    z7 = abs(y-t2)+abs(t2-s1)
    z8 = abs(y-t2)+abs(t2-s2)
    print(min(z1,z2,z3,z4,z5,z6,z7,z8))