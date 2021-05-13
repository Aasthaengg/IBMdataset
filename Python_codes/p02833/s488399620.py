
N = int(input())

if N % 2 == 1:
    print(0)
else:
    ans = 0
    div = 1
    for _ in range(100):
        div *= 5
        ans += N // (div * 2)

    print(ans)
