def main():
    from operator import itemgetter
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=itemgetter(1))

    now = 0
    for a, b in AB:
        if now + a <= b:
            now += a
        else:
            print("No")
            return
    print("Yes")

main()