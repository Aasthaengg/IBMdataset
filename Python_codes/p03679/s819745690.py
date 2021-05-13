def resolve():
    X, A, B = map(int, input().split())
    print("delicious" if A>=B else "dangerous" if A+X<B else "safe")
resolve()