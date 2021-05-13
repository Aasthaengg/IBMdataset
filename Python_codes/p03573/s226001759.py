from collections import Counter
A = Counter(map(int, input().split())).most_common()
print(A[1][0])