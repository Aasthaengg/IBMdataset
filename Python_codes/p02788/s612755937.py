def main():
    import sys
    from collections import deque
    from operator import itemgetter
    b=sys.stdin.buffer
    n,d,a=map(int,b.readline().split())
    m=map(int,b.read().split())
    p,q=deque(),deque()
    f,g=p.popleft,q.popleft
    s=b=0
    for x,h in sorted(zip(m,m),key=itemgetter(0)):
        while p and p[0]<x:
            f()
            b-=g()
        h-=b
        t=0--h//a
        if t>0:
            s+=t
            b+=t*a
            p+=x+d+d,
            q+=t*a,
    print(s)
main()