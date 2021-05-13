def resolve():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    M = int(input())
    T = []
    for __ in range(M):
        t = input()
        T.append(t)
    SS = set(S)
    ans = []
    for i in SS:
        ans.append(S.count(i)-T.count(i))
    print(max(max(ans), 0))
resolve()