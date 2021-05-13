def resolve():
    n = int(input())
    k = int(input())
    pos = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        la = abs(pos[i] - 0)
        lb = abs(pos[i] - k)
        if la <= lb:
            ans += la*2
        else:
            ans += lb*2
    print(ans)
resolve()