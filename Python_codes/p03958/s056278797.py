import sys

k, t = map(int, input().split())
a = list(map(int, input().split()))

if t == 1:
    print(sum(a) - 1)
    sys.exit()

max_a = max(a)

if (sum(a) + 1) // 2 >= max_a:
    print(0)
else:
    print(2 * max_a - sum(a) - 1)