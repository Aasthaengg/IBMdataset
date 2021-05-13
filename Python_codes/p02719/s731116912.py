N,K = map(int,input().split())
A = min(N%K,abs(N%K-K))
print(A)