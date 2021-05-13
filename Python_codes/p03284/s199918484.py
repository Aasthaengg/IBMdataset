N, K = map(int, input().split())

mod = N % K

print(min(1, mod))
