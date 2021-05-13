import sys
H = int(input())
W = int(input())
N = int(input())
X = max(H, W)
Y = min(H, W)
count = 0
total = 0
for _ in range(Y):
    total += X
    count += 1
    if total >= N:
        print(count)
        sys.exit()
for _ in range(X):
    total += Y
    count += 1
    if ctotal >= N:
        print(count)
        break
