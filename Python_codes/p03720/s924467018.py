n, m = map(int, input().split())
c = [0]*n
S = []
for i in range(m):
    a, b = map(int, input().split())
    c[a-1] += 1
    c[b-1] += 1
for i in range(n):
    print(c[i])