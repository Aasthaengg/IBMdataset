N = int(input())
K = int(input())
X = int(input())
Y = int(input())

total = (K * X) + (N - K) * Y
goukei = N * X

if N < K:
    print(goukei)
else:
    print(total)