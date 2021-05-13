N = int(input())
z = [None] * N
w = [None] * N
for i in range(N):
    x, y = map(int, input().split())
    z[i] = x + y
    w[i] = x - y

print(max(max(z)-min(z), max(w)-min(w)))