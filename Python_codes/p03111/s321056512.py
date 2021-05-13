n, a, b, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

from itertools import permutations

def dfs(idx):
    if idx == n:
        return [[[], [], []]]

    ret = []
    for ll in dfs(idx + 1):
        ret.append(ll)

        for i in range(3):
            ll2 = [ll[0][:], ll[1][:], ll[2][:]]
            ll2[i].append(idx)
            ret.append(ll2)

    return ret

lists = dfs(0)

target = [a, b, c]

ans = float('inf')
for _lists in lists:
    if [] not in _lists:

        point = 0
        l = []
        for lis in _lists:
            l.append(sum([x[i] for i in lis]))
            point += 10 * (len(lis) - 1)

        for perm in permutations(l):
            point2 = point
            for i in range(3):
                point2 += abs(target[i] - perm[i])

            ans = min(point2, ans)

print(ans)
