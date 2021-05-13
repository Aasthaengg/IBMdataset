import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,K = LI()
    V = [LI() for _ in range(N)]
    V.sort(key=lambda x:x[1],reverse=True)
    c = [0] * (N+1)
    s = []
    ans = 0
    cnt = 0
    for t,d in V[:K]:
        ans += d
        if c[t] == 0:
            ans += 1 + 2*cnt
            cnt += 1
        else:
            s.append((t,d))
        c[t] = 1

    tmp = ans
    for t,d in V[K:]:
        if s == []: break
        if c[t] == 0:
            x,y = s.pop()
            tmp += d + cnt * 2 + 1 - y
            c[t] = 1
            cnt += 1
            ans = max(tmp,ans)
    print(ans)





if __name__ == '__main__':
    main()