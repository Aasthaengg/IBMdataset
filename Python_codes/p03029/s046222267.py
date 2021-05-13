a, b = list(map(int, input().split()))
n = a * 3 + b
c = n % 2
my_result = (n - c) / 2
print(int(my_result))
