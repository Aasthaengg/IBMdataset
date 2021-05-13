def resolve():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)
    count = 0
    num = 1
    for i in range(N):
        num = A[num-1]
        count += 1
        if num == 2:
            print(count)
            exit()
    print("-1")
resolve()