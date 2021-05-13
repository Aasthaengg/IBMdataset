from collections import Counter

n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
cnt = 0
for k, v in C.items():
    if k <= v:
        cnt += v - k
    else:
        cnt += v
print(cnt)
