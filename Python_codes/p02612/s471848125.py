n = int(input())

if n%1000 != 0:
    print((n//1000 + 1)*1000-n)
else:
    print(0)