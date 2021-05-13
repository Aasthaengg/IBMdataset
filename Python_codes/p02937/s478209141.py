import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    s = SI()
    ds = s + s
    t = SI()

    z = [0] * 26
    nt = [[] for _ in range(len(ds))]

    for i in range(len(ds),0,-1):
        z[ord(ds[i-1])-ord('a')] = i
        nt[i-1] = copy.copy(z)

    rev = 0
    a = 0
    for x in t:
        x = ord(x) - ord('a')
        a = nt[a][x]
        if a == 0:
            print(-1)
            return
        if a >= len(s):
            a -= len(s)
            rev += 1
    print(rev*len(s)+a)

if __name__ == '__main__':
    main()