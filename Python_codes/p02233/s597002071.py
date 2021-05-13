n = int(input())
n1 = 1
n2 = 1
result = 0
if n < 2:
    result = 1
else:
    for i in range(n-1):
        result = n1 + n2
        n2 = n1
        n1 = result
print(result)
