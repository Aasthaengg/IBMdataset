def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = 1000
    sell = False
    buyp = A[0]
    sellp = None
    for i in range(1, N):
        if (not sell) and (buyp > A[i]):
            buyp = A[i]
        elif (not sell):
            sell = True
            sellp = A[i]
        if sell and (sellp < A[i]):
            sellp = A[i]
        elif sell:
            s = m // buyp
            m = s * sellp + (m % buyp)
            buyp = A[i]
            sell = False
    return m
print(main())
