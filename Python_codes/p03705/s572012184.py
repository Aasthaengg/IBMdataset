n, a, b = map(int, input().split())
print(0) if a < b and n < 2 or a > b else print((n-2)*(b-a)+1)