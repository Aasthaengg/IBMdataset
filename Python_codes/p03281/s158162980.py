n = int(input())

result = 0
for i in range(n):
    num = i*2
    if num > n:
        break
    hasndivisors = 0
    for divisor in range(n):
        # print(num+1, divisor+1)
        if (num+1)/(divisor+1) == (num+1)//(divisor+1):
            hasndivisors += 1
    # print(num+1, 'has', hasndivisors, 'divisors')
    if hasndivisors == 8:
        result += 1

print(result)