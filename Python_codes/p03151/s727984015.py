N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
else:
    before = [A[i] - B[i] for i in range(N)]
    before.sort()
    diff = [A[i] - B[i] for i in range(N)]
    # print(diff)
    diff.sort()
    left = 0
    right = N - 1
    while True:
        if diff[left] < 0:
            temp = diff[left]
            diff[left] = min(0, diff[left] + diff[right])
            diff[right] -= diff[left] - temp
        if diff[left] == 0:
            if diff[left + 1] < 0:
                left += 1
        if diff[right] == 0:
            if diff[left] < 0:
                right -= 1
        if diff[left] == 0:
            break
    # print(diff)
    cnt = 0
    for i in range(N):
        if before[i] != diff[i]:
            cnt += 1
    print(cnt)