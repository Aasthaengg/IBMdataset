N = int(input())
K = int(input())
X = int(input())
Y = int(input())
def hotel_price(N,K,X,Y):
    if N<=K:
        return N*X
    else:
        return K*X + (N-K)*Y
print(hotel_price(N,K,X,Y))