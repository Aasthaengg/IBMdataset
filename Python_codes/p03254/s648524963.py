N, x = map(int, input().split())
A = sorted(map(int, input().split()))

if sum(A) == x:
    print(N)

else:
    c = 0
    for ai in A:
        x -= ai
        if x <= 0:
            break
        c += 1

    if c == N:
        print(N - 1)
    else:
        print(c + 1 if x == 0 else c)