n = input()
if len(n) ==1:
    print(int(n))
elif len(n) == 2:
    print(9)
elif len(n) == 3:
    print(9 + int(n) - 100 + 1)
elif len(n) == 4:
    print(9 + 900)
elif len(n)==5:
    print(9 + 900 + int(n) - 10000 + 1)
else:
    print(9 + 900 + 90000)