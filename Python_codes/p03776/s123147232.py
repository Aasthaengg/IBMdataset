import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,A,B = LI()
    v = LI()
    d = {}
    for x in v:
        if x in d: d[x] += 1
        else: d[x] = 1

    dx = sorted(d.items(),reverse=True)

    ans = 0.0
    cnt = 0
    for k in range(A,B+1):
        c = 0
        i = 0
        x = 0
        while c < k:
            c += dx[i][1]
            if c >= k:
                x += dx[i][0] * (dx[i][1] - (c-k))
                cnt_i = math.factorial(dx[i][1]) // math.factorial(c-k) // math.factorial(dx[i][1] - (c-k))
                av = round(x/k,7)
                if av > ans:
                    ans = av
                    cnt = cnt_i
                elif av == ans:
                    cnt += cnt_i
            else:
                x += dx[i][0] * dx[i][1]
            i += 1
    print(ans)
    print(cnt)

if __name__ == '__main__':
    main()