N = int(input())

r = N % 1000
print(0 if r == 0 else 1000 - r)