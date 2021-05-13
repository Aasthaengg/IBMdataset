k, t = map(int, input().split())
a = list(map(int, input().split()))
n = k - max(a)
if max(a) <= k // 2:
    print(0)
else:
    print(k - n * 2 - 1)