N, A, B = map(int, input().split())
if A % 2 == B % 2:
    print(abs(A - B) // 2)
else:
    A_top = A - 1
    B_top = B - 1
    top = (
        B_top + (A - B_top - 1) // 2 if A_top > B_top else A_top + (B - A_top - 1) // 2
    )

    A_btm = N - A
    B_btm = N - B
    btm = (
        B_btm + (N - A - B_btm) // 2 if A_btm > B_btm else A_btm + (N - B - A_btm) // 2
    )
    print(min(top, btm) + 1)
