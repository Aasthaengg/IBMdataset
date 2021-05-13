import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

s = I()
su = [s]
while True:
    if s % 2 == 0:
        s /= 2
    else:
        s = (3*s)+1
    if s in su:
        break
    su.append(s)
print(len(su)+1)