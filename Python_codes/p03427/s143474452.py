m = int(input())
m = str(m + 1)
n = list(m)

if len(n) >= 2:
    if int(n[0]) >= 2:
        print((len(n) - 1) * 9 + int(n[0]) - 1)
    else:
        print((len(n) - 1) * 9)
else:
    print(int(n[0]) - 1)