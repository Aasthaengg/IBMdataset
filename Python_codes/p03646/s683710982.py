import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

def operation(a:list, n:int, idx:int):
    for i,ai in enumerate(a):
        if i==idx:
            a[i] += n
        else:
            a[i] -= 1
            
    return a

k = ni()
mod = k%50

a = [i for i in range(50)]

for m in range(mod):
    a = operation(a,50,m)

geta = k//50

a = [ai+geta for ai in a]

print(50)
print(*a)