N,K = map(int,input().split())
S = K
S *= (K-1)**(N-1)
print(S)