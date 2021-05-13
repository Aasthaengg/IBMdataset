from collections import Counter

N = int(input())

A = []
for _ in range(N):
    A.append(input().strip())

dic = Counter(A)

B = []
for a, c in dic.items():
    B.append((a,c))

B.sort(key=lambda x:x[0])
B.sort(key=lambda x:x[1],reverse=True)

r = B[0][1]
for b in B:
    p, q = b
    if q < r:
        exit()
    print(p)