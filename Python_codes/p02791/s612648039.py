N = int(input())
P = list(map(int, input().split()))
m = P[0]
c = 1
for i in range(1, N):
    if P[i] <= m:
        c += 1
        m = P[i]
print(c)