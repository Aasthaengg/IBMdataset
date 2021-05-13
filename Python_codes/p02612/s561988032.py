a = int(input())
print(1000 - (a % 1000) if a % 1000 != 0 else 0)