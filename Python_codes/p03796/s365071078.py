N = int(input())
num = 1
for i in range(1, N+1):
    num *= i
    num = num % (1000000007)
print(num)