S = input()
a = list(S)
b = []
if len(a) == 2:
    print(S)

elif len(a) == 3:
    b = b + [a[2]] + [a[1]] + [a[0]]
    s = "".join(b)
    print(s)
