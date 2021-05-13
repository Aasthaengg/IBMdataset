n = int(input())


def count_divisors(target):
    _i = 1
    _count = 0
    while _i*_i <= target:
        if target % _i == 0:
            _count += 1
            if _i != target // _i:
                _count += 1
        _i += 1
    return _count


count = 0
for i in range(1, n+1, 2):
    if count_divisors(i) == 8:
        count += 1

print(count)
