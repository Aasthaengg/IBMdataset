from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7
import itertools

def ddprint(x):
  if DBG:
    print(x)

n,c = inm()
d = []
e = []
for i in range(c):
    d.append(inl())
for i in range(n):
    cc = inl()
    cc2 = [x-1 for x in cc]
    e.append(cc2)

s = [ [0]*c for i in range(3) ]
for i in range(n):
    for j in range(n):
        s[(i+j)%3][e[i][j]] += 1
mn = BIG
pm = itertools.permutations(list(range(c)), 3)
for p in pm:
    sm = 0
    for i in range(3):
        for j in range(c):
            sm += s[i][j]*d[j][p[i]]
    mn = min(mn,sm)
print(mn)
