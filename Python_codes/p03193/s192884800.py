N, H, W = list(map(int, input().split()))
A, B = [], []
count = 0
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)
for i, j in zip(A, B):
    if i>=H and j>=W:
        count += 1
print(count)
