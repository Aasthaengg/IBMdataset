N, K = [int(i) for i in input().split()]
print('YES' if sum(divmod(N, 2)) >= K else 'NO')