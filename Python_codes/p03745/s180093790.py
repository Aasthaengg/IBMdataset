# https://atcoder.jp/contests/agc013/tasks/agc013_a


def solve():
    n = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    cur = []
    flag = None
    for a in A:
        if not cur:
            cur.append(a)
            continue
        elif cur[-1] == a:
            cur.append(a)
        elif flag is None:
            if cur[-1] > a:
                flag = False
            elif cur[-1] < a:
                flag = True
            cur.append(a)
            continue
        elif flag:  # increasing
            if cur[-1] > a:
                ans += 1
                cur = [a]
                flag = None
            else:
                cur.append(a)
        elif not flag:  # decreasing
            if cur[-1] < a:
                ans += 1
                cur = [a]
                flag = None
            else:
                cur.append(a)
    if cur:
        ans += 1
    print(ans)


solve()
