N, M = [int(i) for i in input().split()]

tmp = 100 * (N-M) + 1900*M
output = tmp * 2**M
print(output)