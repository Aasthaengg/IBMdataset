a,b = map(int, input().split())
x = 100 * (a-b) + 1900 * b
print(x * (2**b))