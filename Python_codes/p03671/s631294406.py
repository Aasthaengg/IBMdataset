a, b, c = list(map(int, input().split()))
my_result = min(a + b, b + c, c + a)
print(my_result)