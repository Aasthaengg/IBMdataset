N, M = map(int, input().split())
A = list(map(int, input().split()))

print('Yes') if sum(A) / (4 * M) <= sorted(A, reverse=True)[M -1] else print('No')