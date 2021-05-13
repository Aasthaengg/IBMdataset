from functools import lru_cache

@lru_cache(maxsize=None)
def rec_div(i):
    if i < 2:
        return 0
    a, b = divmod(i, 2)
    if b == 0:
        return rec_div(a) + 1
    else:
        return 0
n = input()
l = map(lambda x: rec_div(int(x)), input().split())
print(sum(l))