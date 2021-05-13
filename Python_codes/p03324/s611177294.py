from itertools import count


def count_div_by_100(n: int) -> int:
    for idx in range(4):
        q, r = divmod(n, 100)
        if r != 0:
            return idx
        n //= 100
    return -1


D, N = map(int, input().split())
current = 0
current_idx = 0
for n in count(start=1):
    if count_div_by_100(n) == D:
        current = n
        current_idx += 1
    if current_idx == N:
        print(current)
        break
