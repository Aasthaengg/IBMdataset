N, K = map(int, input().split())
a, b = [], []

for i in range(N):
    a0, b0 = map(int, input().split())
    a.append(a0)
    b.append(b0)

a, b = zip(*sorted(zip(a, b)))
num = 0
for i in range(N):
    num += b[i]
    if num >= K:
        print(a[i])
        break
