def main():
    import sys
    from collections import deque
    from operator import itemgetter
    b=sys.stdin.buffer
    n,d,a=map(int,b.readline().split())
    d*=2
    m=map(int,b.read().split())
    q=deque()
    popleft,append=q.popleft,q.append
    s=b=0
    for x,h in sorted(zip(m,m),key=itemgetter(0)):
        while q and q[0][0]<x:b-=popleft()[1]
        if h>b:
            t=(b-h)//a
            s-=t
            t*=a
            b-=t
            append((x+d,-t))
    print(s)
main()