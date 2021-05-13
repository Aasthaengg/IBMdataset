n,a,b = map(int, input().split())
c = a * n if a * n < b else b
print(c)