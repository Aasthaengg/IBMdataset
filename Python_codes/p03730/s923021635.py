def resolve():
    A, B, C = map(int, input().split())
    flag = 0
    for i in range(1, B+1):
        if (A*i)%B == C:
            flag = 1
    print("YES" if flag == 1 else "NO")
resolve()