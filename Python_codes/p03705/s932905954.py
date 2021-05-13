N, A, B = map(int, input().split())

if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
elif A > B:
    print(0)
else:
    mini = A * (N - 1) + B
    maxi = B * (N - 1) + A
    ans = maxi - mini + 1
    print(ans)