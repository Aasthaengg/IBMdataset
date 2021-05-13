import sys
input = sys.stdin.readline

def m(l):
    l.sort()
    n = len(l)
    
    if n%2==0:
        return (l[n//2-1]+l[n//2])/2
    else:
        return l[n//2]

N = int(input())
A, B = [], []

for _ in range(N):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)
    
l, h = m(A), m(B)

if N%2==0:
    print(int((h-l)*2+1))
else:
    print(h-l+1)