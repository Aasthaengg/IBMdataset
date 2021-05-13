#別解思考
n = int(input())
res = 0
for i in range(1, n // 2 +1):
    res += (int(n / i) * (i + int(n / i) * i)) // 2
res += (n + n // 2 +1) * (n - n // 2 ) //2
print(res)