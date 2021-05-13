a, b = map(int, input().split())
nb = b - a
lb = nb*(nb + 1)//2
print(lb - b)
