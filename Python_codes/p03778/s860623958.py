w,a,b = map(int, input().split())
if a > b: a,b = b,a
if a <= b:
    if a+w < b: print(abs(b-(a+w)))
    else: print(0)