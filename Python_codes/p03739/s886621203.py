n = int(input())
al = list(map(int, input().split()))


def is_diff_sign(s, t):
    return (s > 0 > t) or (s < 0 < t)


def count(_list, first):
    cnt = abs(first - _list[0])
    prev_sum = first
    prev_positive = first > 0
    for a in _list[1:]:
        _sum = prev_sum + a
        if is_diff_sign(prev_sum, _sum):
            prev_sum = _sum
            prev_positive = prev_sum > 0
            continue
        if prev_positive:
            prev_sum = -1
        else:
            prev_sum = 1
        prev_positive = not prev_positive
        cnt += abs(_sum) + 1
    return cnt


ans = 0
if al[0] == 0:
    ans = min(count(al, 1), count(al, -1))
else:
    ans = min(count(al, al[0]), count(al, -al[0] // abs(al[0])))
print(ans)
