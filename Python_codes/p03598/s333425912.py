N,K = (int(input()) for T in range(0,2))
X = [int(T) for T in input().split()]
print(sum(2*min(TX,K-TX) for TX in X))