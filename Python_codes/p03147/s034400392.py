def resolve():
    N = int(input())
    H = list(map(int, input().split()))

    ans = 0
    pre = 0
    for i in H:
        if pre < i:
            ans += i-pre

        pre = i

    print(ans)


resolve()