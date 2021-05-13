def findSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

n = int(input())
minTotal = float('inf')
for i in range(1,n+1):
    if 0 < n - i < n:
        a = findSumOfDigits(i)
        b = findSumOfDigits(n-i)
        if a + b < minTotal:
            minTotal = a + b
print(minTotal)