N, A, B = map(int, input().split())

if A > B:
    print(0)
    exit()
elif A == B:
    print(1)
    exit()
else:
    if N == 1:
        print(0)
        exit()

ans = (B * (N - 1) + A) - (A * (N - 1) + B) + 1
print(ans)
