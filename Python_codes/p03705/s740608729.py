N, A, B = map(int, input().split())
if A > B:
    print(0)
    exit()

if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
    exit()


C = N - 2
l = A * C
h = B * C
print(h - l + 1)