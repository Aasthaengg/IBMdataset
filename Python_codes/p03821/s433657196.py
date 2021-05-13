N = int(input())
a = []
b = []
for _ in range(N):
    ab = list(map(int, input().split()))
    a.append(ab[0])
    b.append(ab[1])

count = 0
for i in range(N-1, -1, -1):
    if (a[i]+count) % b[i] != 0:
        count += (b[i] - (a[i]+count) % b[i])
print(count)
