def main():
    import sys
    from collections import deque
    from operator import itemgetter
    b=sys.stdin.buffer
    n,d,a=map(int,b.readline().split())
    m=map(int,b.read().split())
    p,q=deque(),deque()
    pl,ql=p.popleft,q.popleft
    pa,qa=p.append,q.append
    s=b=0
    for x,h in sorted(zip(m,m),key=itemgetter(0)):
        while p and p[0]<x:
            pl()
            b-=ql()
        h-=b
        t=-(-h//a)
        if t>0:
            s+=t
            t*=a
            b+=t
            pa(x+d+d)
            qa(t)
    print(s)
main()