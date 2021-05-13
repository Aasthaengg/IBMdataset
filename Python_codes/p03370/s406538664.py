N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
m.sort()
X = X - sum(m)
donut = N
for i in m:
    if X // i > 0:
        donut += X // i
        X = X % i
    else:
        break
print(donut)