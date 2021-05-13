def resolve():
    N = int(input())
    T, A = [int(i) for i in input().split()]
    H = [int(i) for i in input().split()]
    absList = []
    for i in range(N):
        absList.append((abs(A - (T - (H[i] * 0.006))), i))
    print(min(absList)[1] + 1)


resolve()
