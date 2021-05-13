n = int(input())
P = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    T = sorted(P[i - 1: i + 2])
    if T[1] == P[i]:
        count += 1
print(count)