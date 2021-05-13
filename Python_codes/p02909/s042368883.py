S = input()
W = ['Sunny', 'Cloudy', 'Rainy']
N = W.index(S) + 1
if N == 3:
    print(W[0])
else:
    print(W[N])