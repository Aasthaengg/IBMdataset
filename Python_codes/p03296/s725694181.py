def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    count = 1
    for i in range(N-1):
        if A[i] == A[i+1]:
            count += 1
        else:
            if count > 1:
                ans += count//2
            count = 1
    if count > 1:
        ans += count//2
    print(ans)
resolve()