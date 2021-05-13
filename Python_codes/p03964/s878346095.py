import sys

input = sys.stdin.readline


def main():
    N = int(input())
    TA = [[int(x) for x in input().split()] for _ in range(N)]

    now = TA[0]
    for t, a in TA[1:]:
        i = max(now[0] //t , now[1] // a)
        while now[0] > t * i or now[1] > a * i:
            i += 1
        now[0] = t * i
        now[1] = a * i

    print(now[0] + now[1])


if __name__ == '__main__':
    main()
