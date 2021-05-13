N = int(input())
a = list(map(int, input().split()))
b = []

S = 0
for i in range(N):
    S = S^a[i]

for j in range(N):
    b.append(S^a[j])

print(*b)