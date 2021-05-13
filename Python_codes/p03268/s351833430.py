N, K = map(int, input().split())

if (K % 2) == 1:
    count = N // K
    print(count**3)
else:
    count1 = N // K
    count2 = 0
    for i in range(N + 1):
        if (i % K) == (K / 2):
            count2 += 1
    # print(count1, count2)
    print(count1**3 + count2**3)