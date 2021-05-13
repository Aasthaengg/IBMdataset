w, a, b  = map(int, input().split())
if a <= b <= a+w or a <= b+w <= a+w:
    print(0)
else:
    res = float("inf")
    res = min(res, abs(b-(a+w)))
    res = min(res, abs(a-(b+w)))
    print(res)