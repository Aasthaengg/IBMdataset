a, b, c = list(map(int, input().split()))
n = c % a
my_result = b * (c - n) / a
print(int(my_result))