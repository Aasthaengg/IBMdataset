a, b = map(int, input().split())

big = max(a+b, a-b)
print(max(big, a*b))