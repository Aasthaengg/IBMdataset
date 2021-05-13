x,k,d = map(int,input().split())
result = 0
if abs(x) > k * d:
    result = abs(x) - k*d
else:
    g = abs(x) // d
    if (k - g) % 2 == 0:
        result = abs(x) - d*g
    else:
        result = d*(g+1) - abs(x)
print(result)