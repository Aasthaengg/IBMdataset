import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

s = S()
N = len(s)
if s != s[::-1]:
    print("No")
else:
    ss = s[:(N-1)//2]
    if ss != ss[::-1]:
        print("No")
    else:
        sss = s[((N+3)//2)-1:]
        if sss != sss[::-1]:
            print("No")
        else:
            print("Yes")
