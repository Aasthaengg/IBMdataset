W, a, b = map(int,input().split())
# N = int(input())
# al = list(map(int,input().split()))


if a <= b:
    if b-(a+W) >= 0:
        print(b-(a+W))
    else:
        print(0)
else:
    if a - (b+W) >= 0:
        print(a - (b+W))
    else:
        print(0)