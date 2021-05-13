import sys
from collections import deque

def main(sa,sb,sc):
    sa=deque(sa)
    sb=deque(sb)
    sc=deque(sc)
    ms={'a':sa, 'b':sb, 'c':sc}
    ct='a'
    while True:
        cc=ms[ct].popleft()
        ct=cc
        if not ms[ct]:
            return ct.upper() 

sa=sys.stdin.readline().strip()
sb=sys.stdin.readline().strip()
sc=sys.stdin.readline().strip()

print(main(sa,sb,sc))
