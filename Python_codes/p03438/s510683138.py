def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt_a = 0
    cnt_b = 0
    for a, b in zip(A, B):
        if a > b:
            cnt_a += a - b
        elif a < b:
            cnt_b += (b - a) // 2

    if cnt_a > cnt_b:
        return "No"
    else:
        return "Yes"


print(solve())
