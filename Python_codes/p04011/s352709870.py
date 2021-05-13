N = int(input())
K = int(input())
X = int(input())
Y = int(input())

print(sum([X if K >= i else Y for i in range(1, N+1)]))