from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
print('YES' if len(cnt) == N else 'NO')
