a = list(input())

if len(a) == 2:
    a = "".join(a)
    print(a)
else:
    a.reverse()
    a = "".join(a)
    print(a)