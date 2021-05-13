import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    n,m,d = LI()

    x = ((n-d) / n) * (1/n)
    if d > 0: x *= 2
    ans = x * (m-1)
    print(ans)


if __name__ == '__main__':
    main()