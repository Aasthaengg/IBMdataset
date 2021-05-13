A, B, C = map(int, input().split())
K = int(input())

_sum = []
_max = max(A, B, C)
remaining = [r for r in [A, B, C] if r != _max]
if len(remaining) == 0:
    remaining = [_max, _max]
if len(remaining) == 1:
    remaining.append(_max)

for i in range(K):
    _max = _max * 2

print(_max + sum(remaining))
