def resolve():
    n = int(input())
    pos = list(map(int, input().split()))
    pos.sort()

    ans = pos[-1] - pos[0]

    print(ans)
resolve()