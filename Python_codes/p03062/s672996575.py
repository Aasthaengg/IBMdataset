
N = int(input())
X = list(map(int, input().split()))

y = [abs(v) for v in X]
if sum(v < 0 for v in X) % 2 == 0:
    print(sum(y))
else:
    print(sum(y) - 2 * min(y))
