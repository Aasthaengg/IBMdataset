n = input()

intn = int(n)

if len(n) == 1:
    print(intn)
elif len(n) == 2:
    print("9")
elif len(n) == 3:
    print(intn - 100 + 1 + 9)
elif len(n) == 4:
    print(900+9)
elif len(n) == 5:
    print(intn - 10000+ 1 + 900 +9)
else:
    print("90909")