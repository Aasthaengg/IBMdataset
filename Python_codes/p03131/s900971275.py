K, A, B = map(int, input().split())
if A > B - 2 or K < A + 1:
    print(1 + K)
else:
    K -= A - 1
    cnt = K // 2 * B - (K // 2 - 1) * A
    if K % 2:
        cnt += 1
    print(cnt)

