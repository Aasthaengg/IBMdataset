N = int(input())
print('Yes' if sum(4 * x + 7 * y == N for x in range(N//4 + 1) for y in range(N//7 + 1)) > 0 else 'No')