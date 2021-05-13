import sys, math, bisect
sys.setrecursionlimit(200010)

def input():
    return sys.stdin.readline()[:-1]

def main():
    A, B, Q = map(int,input().split())
    s = [-10**12] + sorted([int(input()) for k in range(A)]) + [10**12]
    t = [-10**12] + sorted([int(input()) for k in range(B)]) + [10**12]
    for _ in range(Q):
        q = int(input())
        s1 = s[bisect.bisect_left(s,q)]
        s2 = s[bisect.bisect_left(s,q)-1]
        t1 = t[bisect.bisect_left(t,q)]
        t2 = t[bisect.bisect_left(t,q)-1]
        d1 = max(q-s2,q-t2)
        d2 = max(s1-q,t1-q)
        d3 = 2*(q-s2)+t1-q
        d4 = 2*(q-t2)+s1-q
        d5 = 2*(s1-q)+q-t2
        d6 = 2*(t1-q)+q-s2
        print(min(d1,d2,d3,d4,d5,d6))

if __name__ == '__main__':
    main()
