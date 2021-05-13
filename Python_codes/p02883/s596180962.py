def resolve():
    N, K = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))
    F = sorted(list(map(int, input().split())), reverse=True)
    q = []
    for i in range(N):
        q.append((A[i]*F[i], A[i], F[i]))

    def isok(time):
        total = 0
        for t, a, f in q:
            acc = time // f
            if acc < a:
                total += a - acc
        return True if total <= K else False

    left = -1
    right = A[-1]*F[0]
    while (right - left > 1):
        mid = left + (right - left) // 2
        if isok(mid):
            right = mid
        else:
            left = mid
    print(right)

    
if __name__ == "__main__":
    resolve()
