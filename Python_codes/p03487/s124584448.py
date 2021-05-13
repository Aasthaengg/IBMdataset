from collections import Counter
N = int(input())
A = map(int, input().split())
A = Counter(A)

cnt = 0
for i, j in A.items():
    if i > j:
        cnt += j
    elif i < j:
        cnt += j-i
print(cnt)
