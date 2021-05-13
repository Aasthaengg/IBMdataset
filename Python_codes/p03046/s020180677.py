M, K = map(int, input().split())

if K >= 2 ** M:
    print(-1)
elif M == 0:
    print("0 0" if K == 0 else -1)
elif M == 1:
    print("1 0 0 1" if K == 0 else -1)
else:
    A = [str(i) for i in range(2 ** M) if i != K]
    print(" ".join(A), K, " ".join(reversed(A)), K)
