a, b, c = map(int, input().split())

sum1 = a + b
sum2 = a + c
sum3 = b + c

print(min(sum1, sum2, sum3))