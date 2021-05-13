a, b = list(map(int, input().split()))
n = a + b
k = n % 2
my_result = (n + k) / 2
print(int(my_result))