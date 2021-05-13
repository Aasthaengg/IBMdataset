n, m = map(int, input().split())
p = 10 ** 9 + 7
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]
XX = [(X[i + 1] - X[i]) * (n - i - 1) * (i + 1) % p for i in range(n - 1)]
YY = [(Y[j + 1] - Y[j]) * (m - j - 1) * (j + 1) % p for j in range(m - 1)]
print(sum(XX) * sum(YY) % p)
