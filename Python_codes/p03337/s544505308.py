a, b = list(map(int, input().split()))
my_result = max(a + b, a - b, a * b)
print(my_result)