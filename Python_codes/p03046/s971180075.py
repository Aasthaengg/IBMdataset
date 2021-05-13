M, K = map(int, input().split())

if K >= 2 ** M:
    print(-1)
    quit()

if M == 0:
    if K == 0:
        print('0 0')
elif M == 1:
    if K == 0:
        print('0 0 1 1')
    if K == 1:
        print(-1)
else:
    b = [str(i) for i in range(2**M) if i != K]
    c = [str(i) for i in range(2**M-1, -1, -1) if i != K]
    print(' '.join(b) + ' ' + str(K) + ' ' + ' '.join(c) + ' ' + str(K))