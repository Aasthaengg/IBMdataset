N,K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = -(-(N-1) // (K-1))
print(ans)