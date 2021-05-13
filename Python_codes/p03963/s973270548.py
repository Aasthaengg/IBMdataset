def resolve():
    N, M = map(int, input().split())
    print(M*(M-1)**(N-1))
resolve()