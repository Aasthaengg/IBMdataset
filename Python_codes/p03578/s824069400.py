from collections import defaultdict


def solve():
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))
    cnt = defaultdict(int)
    for d in D:
        cnt[d] += 1
    for t in T:
        if cnt[t] <= 0:
            print('NO')
            return
        cnt[t] -= 1
    print('YES')


if __name__ == "__main__":
    solve()
