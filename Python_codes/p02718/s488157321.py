N, M = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]
th = sum(A) / (4 * M)
print('Yes' if len([a for a in A if a >= th]) >= M else 'No')
