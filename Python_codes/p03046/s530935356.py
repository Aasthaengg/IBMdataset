M, K = map(int, input().split())
if K >= 2 ** M:
    print(-1)
    exit(0)
if M == 1:
    if K == 1:
        print(-1)
    else:
        print('0 0 1 1')
    exit(0)
A = [i for i in range(2 ** M) if i != K]
print(' '.join(str(a) for a in A), K, ' '.join(str(a) for a in reversed(A)), K)
