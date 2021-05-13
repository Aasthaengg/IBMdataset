i = input().split()

a,b = list(map(int, i))

if a >= 13:
    print(int(b))
elif a <= 5:
    print(0)
else:
    print(int(b/2))