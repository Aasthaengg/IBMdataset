data = []

data.extend(list(map(int, input().split(" "))))
N = data[0]
K = data[1]

if K == 1:
    print(0)
else:
    print(N - K)