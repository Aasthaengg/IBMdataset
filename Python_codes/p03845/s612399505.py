
n = int(input())
t = list(map(int, input().split()))
m = int(input())
p, x = zip(*[map(int, input().split()) for _ in range(m)])

sum_dflt = sum(t)
for i in range(m):
    print(sum_dflt - t[p[i] - 1] + x[i])
