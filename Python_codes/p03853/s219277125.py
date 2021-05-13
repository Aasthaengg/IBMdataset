from sys import stdin
def S(): return stdin.readline().rstrip()
def LI(): return list(map(int,stdin.readline().rstrip().split()))

tmp = LI()
h,w = [tmp.pop(0) for i in range(2)]

c = []

for i in range(h):
    tmp = S()
    c.append(tmp)

for i in range(h):
    for k in range(2):
        print(c[i],end='')
        print()
