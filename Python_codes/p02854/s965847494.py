def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    mid = 0
    diff = float("inf")
    total = sum(A)
    p = 0
    # print(total)
    for i in range(n):
        # print("i:",i, "total:", total, "p:", p, "diff:", diff)
        if abs(total-p) < diff:
            diff = abs(total - p)
            mid = i
        p += A[i]
        total -= A[i]
    front = A[:mid] 
    back =  A[mid:]
    print(abs(sum(front)-sum(back)))
resolve()