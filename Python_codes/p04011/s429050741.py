N = int(input())
K = int(input())
X = int(input())
Y = int(input())

def goukei(N,K,X,Y):
    money = 0
    if N > K:
        for i in range(K):
            money += X
    else:
        for i in range(N):
            money += X
    if N - K > 0:
        for j in range(N-K):
            money += Y
    return money

print(goukei(N,K,X,Y))