def resolve():
    N = int(input())
    A = [int(i) for i in input().split()]
    cnt = 1
    for a in A:
        if a % 2 == 0:
            cnt *= 2
    print(3**N - cnt)


resolve()
