N = int(input())
K = int(input())
X = [int(x) for x in input().split()]

s = 0
for x in X:
    s += min(x, K - x)

print(s * 2)
