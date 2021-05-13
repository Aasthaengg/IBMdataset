a, b, c = map(int, input().split())
print(0 if a * b * c % 2 == 0 else a * b * c // max(a, b, c) )
