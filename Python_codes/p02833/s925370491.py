def input_li():
    return list(map(int, input().split()))

def input_int():
    return int(input())

N = input_int()
if N % 2 == 0:
    ans = 0
    N //= 2
    while N > 0:
        ans += N // 5
        N //= 5
    print(ans)
else:
    print(0)
