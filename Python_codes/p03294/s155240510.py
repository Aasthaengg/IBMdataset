def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A)-N)
resolve()