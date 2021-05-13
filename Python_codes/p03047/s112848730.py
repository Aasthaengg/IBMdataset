def LI():
    return list(map(int, input().split()))


N, K = LI()
print(N-K+1)
