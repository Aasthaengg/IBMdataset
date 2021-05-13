def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    ave = sum(A)/N
    this = max(A)
    count = 0
    for i in A:
        ans.append(abs(ave-i))
    for j in range(N):
        if this > ans[j]:
            count = j
            this = ans[j]
    print(count)
resolve()