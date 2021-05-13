import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,K = LI()
    sa = (N - 1) * (N - 2) // 2 - K
    if sa < 0:
        print(-1)
        return

    ans = []
    for i in range(2,N+1):
        ans.append((1,i))
    i = 2
    j = 3
    while sa > 0:
        ans.append((i,j))
        sa -= 1
        j += 1
        if j > N:
            i += 1
            j = i + 1
    print(len(ans))
    for x in ans:
        print(x[0],x[1])

if __name__ == '__main__':
    main()