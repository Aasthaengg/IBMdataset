a, b = map(int, input().split())
if 6 <= a <= 12:
    b = b/2
elif a<6:
    b = 0
print(int(b))
