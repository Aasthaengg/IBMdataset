N, x = map(int, input().split())
a = sorted(map(int, input().split()))

if sum(a) > x:
    while sum(a) > x:
        del a[-1]
    print(len(a))
else:
    print(N) if sum(a) == x else print(N-1)