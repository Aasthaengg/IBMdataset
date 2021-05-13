# ＤＦＳ, パターン列挙_各竹の使用パターンを列挙

n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

stack = [[0],[1],[2],[-1]]

ans = 10**9
while stack:
    tmp = stack.pop()
    if len(tmp) == n:
        if 0 not in tmp or 1 not in tmp or 2 not in tmp:
            continue
        abc = [0, 0, 0, -30]
        for j in range(n):
            if tmp[j] >= 0:
                abc[tmp[j]] += l[j]
                abc[3] += 10
        mp = abc[3]
        mp += abs(abc[0] - a)
        mp += abs(abc[1] - b)
        mp += abs(abc[2] - c)
        ans = min(ans, mp)

    elif len(tmp) < n:
        w = tmp + [0]
        x = tmp + [1]
        y = tmp + [2]
        z = tmp + [-1]
        stack += [w, x, y, z]

print(ans)
