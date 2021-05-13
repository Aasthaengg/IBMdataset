#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    N = int(input())
    S = input()
    cnt0 = S.count("1")

    if cnt0 == 0:
        print("\n".join(map(str, [1]*N)))
        return

    X = int(S, 2)

    def f2():
        cache = [0] * (cnt0 + 1)
        i = 1
        bi = []
        while i <= cnt0:
            bi.append(i)
            i <<= 1
        from collections import deque
        dq = deque([(0, 0, 0)])
        ls = len(bi) -1
        while dq:
            i, x, cnt = dq.popleft()

            cnt += 1
            for j in range(i, ls):
                y = x | bi[j]

                if y > cnt0: break

                cache[y] = cache[y % cnt] + 1

                j += 1
                dq.append((j, y, cnt))
            else:
                y = x | bi[ls]
                if y > cnt0: continue
                cache[y] = cache[y % cnt] + 1
        return cache


    memo = f2()

    dc = []
    for v in [1, -1]:
        x = cnt0 + v
        y = X % x if x else 0
        dc.append((x, v, y, [1, N-1]))

    ans = [0] * N
    for i in reversed(range(N)):
        cnt, v, n, m1 = dc[0 if S[i] == "0" else 1]

        if cnt == 0:
            ans[i] = 0
            continue

        m2 = (m1[0]<<(m1[1]-i)) % cnt
        n = (n + v*m2) % cnt
        m1[0], m1[1] =  m2, i

        ans[i] = 1 + memo[n]

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    resolve()
