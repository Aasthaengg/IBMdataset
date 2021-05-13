N = int(input())
K = int(input())
X = map(int, input().split())
res = 0
for i, x in enumerate(X):
    res += min(2*(x), 2*abs(x-K))
print(res)