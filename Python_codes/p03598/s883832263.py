N = int(input())
K = int(input())
X = list(map(int, input().split()))

sum = 0

for x in X:
    sum += 2*min(x, K-x)

print(sum)