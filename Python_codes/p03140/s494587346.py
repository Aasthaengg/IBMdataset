def nikkei19q_b():
    N = int(input())
    A = str(input())
    B = str(input())
    C = str(input())
    ans = 0
    for i in range(N):
        chset = set([A[i], B[i], C[i]])
        change = len(chset) - 1
        ans += change
    print(ans)

nikkei19q_b()