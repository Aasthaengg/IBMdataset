S = input()
W = ['Sunny','Cloudy','Rainy']

if S == W[0] or S == W[1]:
    print(W[W.index(S)+1])
else:
    print(W[0])

