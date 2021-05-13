import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N,A,B = LI()
    H = [NI() for _ in range(N)]

    h = max(H) // B + 1
    l = 0
    while h > l+1:
        m = (h+l) // 2
        cnt = m
        for x in H:
            if x >= m * B:
                cnt -= math.ceil((x-m*B) / (A-B))
                if cnt < 0: break
        else:
            h = m
            continue
        l = m
    print(h)

if __name__ == '__main__':
    main()