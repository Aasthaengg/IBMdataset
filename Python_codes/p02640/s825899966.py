X, Y = map(int, input().split())
print('Yes' if any([2*i + 4*(X-i) == Y for i in range(X+1)]) else 'No')