s = input().split()

a = int(s[0])
b = int(s[1])

if a >= 13:
    print(b)
elif a <= 5:
    print("0")
else:
    print(int(b / 2))