N = int(input())
K = int(input())

X = [int(x) for x in input().split(" ")]
res = 0
for x in X:
    res += min(abs(x - K), x) * 2
print(res)
