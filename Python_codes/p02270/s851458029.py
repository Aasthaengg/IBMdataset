import sys
input = sys.stdin.readline


def is_loadable(pack: list, k: int, P: int):
    _tmp = 0
    counter = 1
    for w in pack:
        if _tmp + w > P:
            _tmp = w
            counter += 1
        else:
            _tmp += w
        if counter > k or w > P:
            return False
    return True


n, k = [int(i) for i in input().strip().split()]
pack = [None] * n
for i in range(n):
    pack[i] = int(input())

right = sum(pack)
left = max(pack)

while left < right:
    mid = (left + right) // 2
    if is_loadable(pack, k, mid):
        right = mid
    else:
        left = mid + 1

print(left)

