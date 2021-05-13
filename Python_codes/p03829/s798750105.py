import sys
input = sys.stdin.readline
N, A, B = [int(x) for x in input().strip().split()]
X = [int(x) for x in input().strip().split()]
p = X[0]
ans = 0
for x in X[1:]:
    c = (x - p) * A
    if c <= B:
        ans += c
    else:
        ans += B
    p = x
print(ans)