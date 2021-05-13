import sys
# sys.setrecursionlimit(100000)
from collections import deque


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S_deq = deque(list(input()))
    cnt = 0
    while S_deq:
        # 残り1文字のとき
        if len(S_deq) == 1:
            S_deq.pop()
        # 両端が同じ文字のとき
        elif S_deq[0] == S_deq[-1]:
            S_deq.popleft()
            S_deq.pop()
        # 片方が x のとき
        elif S_deq[0] == "x":
            S_deq.popleft()
            cnt += 1
        elif S_deq[-1] == "x":
            S_deq.pop()
            cnt += 1
        else:
            print(-1)
            return
    print(cnt)
    return


if __name__ == "__main__":
    main()
