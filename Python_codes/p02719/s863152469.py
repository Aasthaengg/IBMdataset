N,K = [int(i) for i in input().split()]

while N > K:
    N %= K

print(min(N,abs(N-K)))
