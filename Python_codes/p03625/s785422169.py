import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    a = list(map(int, readline().split()))

    a.sort(reverse=True)

    e1 = 0
    e2 = 0
    prev = 0
    
    for cur in a:
        if prev == cur:
            if e1 == 0:
                e1 = cur
            else:
                e2 = cur
                print(e1*e2)
                sys.exit()
            cur = 0
        prev = cur

    print(0)

if __name__ == '__main__':
    main()
