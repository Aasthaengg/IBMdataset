import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    # https://scrapbox.io/fukucchi/%E6%8B%AC%E5%BC%A7%E5%88%97%E3%81%AE%E6%95%B4%E5%90%88%E6%80%A7%E5%95%8F%E9%A1%8C
    # https://atcoder.jp/contests/abc064/tasks/abc064_d

    X = str(input())
    N = len(X)
    stack_rem = 0
    need_left = 0
    pop_cnt = 0

    for i in range(N):
        if X[i] == 'S':
            stack_rem += 1
        elif stack_rem > 0:
            stack_rem -= 1
            pop_cnt += 1
    print(N-pop_cnt*2)


resolve()