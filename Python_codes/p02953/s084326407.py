def resolve():
    N = int(input())
    H = list(reversed([int(i) for i in input().split()]))
    for i in range(N - 1):
        if H[i + 1] > H[i] + 1:
            print("No")
            return
        elif H[i + 1] == H[i] + 1:
            H[i + 1] -= 1
    else:
        print("Yes")


resolve()
