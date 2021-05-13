def push(X):
    coin=X
    X-=1
    return X,coin
A,B=map(int,input().split())
coin=0
if A>B:
    A,coin=push(A)
else:
    B,coin=push(B)
if A>B:
    coin+=A
else:
    coin+=B
print(coin)