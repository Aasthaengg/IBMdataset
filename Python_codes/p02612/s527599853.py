x = int(input())
out = 1000 - x % 1000 if x % 1000 != 0 else 0
print(out)
