n = int(input())
result = 1
limit = 10**9+7
for i in range(1, n+1):
    result = result*i % limit
print(result)
