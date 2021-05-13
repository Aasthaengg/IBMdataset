import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque

    a = input()
    b = input()
    c = input()

    aq = deque(a)
    bq = deque(b)
    cq = deque(c)

    turn = "a"

    while True:
        if turn == "a":
            if not aq:
                return print("A")
            turn = aq.popleft()
        elif turn == "b":
            if not bq:
                return print("B")
            turn = bq.popleft()
        else:
            if not cq:
                return print("C")
            turn = cq.popleft()


if __name__ == '__main__':
    main()
