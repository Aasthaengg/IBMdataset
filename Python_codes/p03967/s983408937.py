import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**5
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    s = sys.stdin.readline().rstrip()
    n = len(s)
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == 'p': ans -= 1
        else:
            if s[i] == 'g': ans += 1
    print(ans)

if __name__ == '__main__':
    main()