def resolve():
    A, B, K = list(map(int, input().split()))
    mx = min(A, B)
    ans = []
    for i in range(1, mx+1):
        if A % i == 0 and B % i == 0:
            ans.append(i)
    print(ans[-K])
    return

resolve()