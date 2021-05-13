X, K, D = [int(x) for x in input().split(" ")]

result = 0
if abs(X) > K * D:
    result = abs(X) - K * D
else:
    y = int(round(abs(X) / D))
    resX = abs(abs(X) - D * y)
    resK = K - y
    if resK % 2 == 1:
        result = abs(resX - D)
    else:
        result = resX
print(result)
