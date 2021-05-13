def resolve():
    N = int(input())
    A, B = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [0, 0, 0]
    for i in range(N):
        if P[i] <= A:
            ans[0] += 1
        elif P[i] >= B+1:
            ans[2] += 1
        else:
            ans[1] += 1
    print(min(ans))
resolve()