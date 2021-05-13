N = int(input())
A = list(map(int, input().split()))

A_i = [A[i] - i - 1 for i in range(N)]
A_i.sort()
if N % 2 == 1:
    b = A_i[N // 2]
    ans = 0
    for a in A_i:
        ans += abs(a - b)

    print(ans)
else:
    b1 = A_i[N // 2]
    b2 = A_i[N // 2 - 1]
    ans1 = 0
    ans2 = 0
    for a in A_i:
        ans1 += abs(a - b1)
        ans2 += abs(a - b2)
    print(min(ans1, ans2))
