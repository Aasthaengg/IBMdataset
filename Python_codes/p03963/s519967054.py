N,K=map(int,input().split())
print(K*(K-1)**(N-1) if N>=2 else K)