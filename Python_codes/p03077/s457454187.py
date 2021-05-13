def resolve():
    N, *AE = [int(input()) for _ in range(6)]
    print(-(-N // min(AE)) + 4)


resolve()
