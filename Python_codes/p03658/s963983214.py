def actual(N, K, L):
    return sum(sorted(L)[-K:])

N, K = map(int, input().split())
L = map(int, input().split())

print(actual(N, K, L))