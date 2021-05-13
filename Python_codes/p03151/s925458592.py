N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [a - b for a, b in zip(A, B)]
diff.sort()
if sum(A) < sum(B):
    print(-1)
else:
    minus_sum = 0
    ans = 0
    for i in range(N):
        if diff[i] < 0:
            minus_sum += diff[i]
            ans += 1
        else:
            break

    for i in range(N - 1, 0, -1):
        if minus_sum >= 0:
            break
        else:
            ans += 1
            minus_sum += diff[i]

    print(ans)
