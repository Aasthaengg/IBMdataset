N = int(input())
X = list(map(int, input().split()))

cnt = 0
mini = float('inf')

P = max(X) + 1

for i in range(P):
    for j in range(len(X)):
        cnt += (X[j] - i)**2
    if cnt < mini:
        mini = cnt
    cnt = 0

print(mini)