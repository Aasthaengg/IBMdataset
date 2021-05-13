import math

n, p = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))

zero_count = 0
one_count = 0

for num in a:
    if num % 2 == 0:
        zero_count += 1
    else:
        one_count += 1

coef = 2 ** zero_count

ans = 0

for i in range(one_count + 1):
    if i % 2 != p:
        continue
        
    ans += math.factorial(one_count) // math.factorial(one_count - i) // math.factorial(i)
print(ans * coef)
        
