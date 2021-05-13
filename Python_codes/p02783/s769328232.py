def resolve():
    h, a = list(map(int, input().split()))

    ans = h // a
    ans += 0 if h % a == 0 else 1
    print(ans)
resolve()