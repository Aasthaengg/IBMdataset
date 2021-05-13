n, a, b = map(int, input().split())
if b < a or (a != b and n == 1):
    print(0)
    exit()
if a == b:
    print(1)
    exit()
_min = a*(n-1)+b
_max = a+b*(n-1)
ans = _max - _min + 1
print(ans)
