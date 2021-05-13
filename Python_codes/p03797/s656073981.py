N, M = map(int, input().split())
if N == 0:
    print(0)
elif N >= M:
    print(M // 2)
else:
    ret = N
    M -= N * 2
    ret += M // 4
    print(ret)
