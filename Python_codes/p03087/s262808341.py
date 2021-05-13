def resolve():
    import sys
    input = sys.stdin.readline
    N, Q = [int(i) for i in input().split()]
    S = input()
    pre = [0 for _ in range(N)]
    for i in range(N - 1):
        pre[i + 1] = pre[i] + (1 if S[i:i + 2] == "AC" else 0)
    for _ in range(Q):
        l, r = [int(i) for i in input().split()]
        print(pre[r - 1] - pre[l - 1])


resolve()
