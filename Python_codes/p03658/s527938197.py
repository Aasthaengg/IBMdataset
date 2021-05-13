def resolve():
    N, K = map(int, input().split())
    long = list(map(int, input().split()))
    L = sorted(long)[K*-1:]
    print(sum(L))
resolve()