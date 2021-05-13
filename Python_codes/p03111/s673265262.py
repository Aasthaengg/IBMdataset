import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**4
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N,A,B,C = LI()
    l = [NI() for _ in range(N)]
    x = [0] * 3
    ans = INF
    for p in itertools.combinations(range(N),3):
        q = []
        for i in range(N):
            if not i in p: q.append(i)
        for i in range(4**(N-3)):
            for j in range(3): x[j] = l[p[j]]
            mp = 0
            r = i
            for j in range(N-3):
                k = r % 4
                if k > 0:
                    x[k-1] += l[q[j]]
                    mp += 10
                r //= 4
            for a,b,c in itertools.permutations(x):
                ans = min(ans,mp+abs(A-a)+abs(B-b)+abs(C-c))

    print(ans)



if __name__ == '__main__':
    main()