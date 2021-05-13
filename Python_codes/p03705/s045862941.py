N, A, B = map(int, input().split())

if A > B:
    ans = 0
else:
    if N == 1:
        if A == B:
            ans = 1
        else:
            ans = 0
    elif N == 2:
        if A == B:
            ans = 1
        else:
            ans = B - A + 1
    else:
        ans = (N - 2) * B - (N - 2) * A + 1

print(ans)