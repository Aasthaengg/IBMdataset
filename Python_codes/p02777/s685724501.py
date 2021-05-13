import sys
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
def ISS(): return sys.stdin.readline().rstrip().split()

s, t=ISS()
a, b=ISI()
u=input()
if u==s: a-=1
else:b-=1
print(a, b)