# coding: utf-8

n = int(input().rstrip())

monsters = list(reversed(sorted(map(int, input().rstrip().split(" ")))))

cnt = [0 for i in range(n)]
cnt[n - 1] = monsters[n - 1]
for i in reversed(range(n - 1)):
    cnt[i] = cnt[i + 1] + monsters[i]

dic = {}


def can_alife(idx: int):
    if idx == 0:
        return True
    if idx in dic:
        return dic[idx]

    ret = False
    if monsters[idx - 1] <= cnt[idx] * 2:
        ret = can_alife(idx - 1)
    dic[idx] = ret
    return ret


ans = len([i for i in range(n) if can_alife(i)])
print(ans)
