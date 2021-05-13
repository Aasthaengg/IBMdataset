N = int(input())
K = int(input())
X = list(map(int, input().split()))

c = 0
for x in X:
    s = min(K - x, x)
    c += s * 2

print(c)
