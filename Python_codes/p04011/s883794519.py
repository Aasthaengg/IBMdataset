N,K,X,Y= [int(input()) for i in range (4)]
if N > K:
    yen1 = K * X
    yen2 = (N - K) * Y
    print(yen1 + yen2)
else:
    print(N * X)