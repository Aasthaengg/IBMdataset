from collections import defaultdict
n = int(input())
A = defaultdict(int)
for i in range(n):
    a = int(input())
    if A[a] == 1:
        A[a] = 0
    else:
        A[a] = 1
print(sum(A.values()))
