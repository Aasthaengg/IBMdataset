A, B, K = map(int, input().split())
l = []
for i in range(K):
    if A+i <= B:
        l.append(A+i)
    if B-i >= A:
        l.append(B-i)

for i in sorted(set(l)):
    print(i)