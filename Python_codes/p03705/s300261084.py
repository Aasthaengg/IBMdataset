N, A, B = map(int, input().split())
if A > B:
    print(0)
    exit()
else:
    if N == 1:
        if A != B:
            print(0)
            exit()
        else:
            print(1)
            exit()
    else:
        # (N-1)*A+B以上 A+(N-1)*B以下の全ての値が可能
        ans = (N - 2) * (B - A) + 1
        print(ans)
