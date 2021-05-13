N,K,X,Y= [int(input()) for i in range (4)]
if N > K:
    print(K * X + (N - K) * Y)
else:
    print(N * X)