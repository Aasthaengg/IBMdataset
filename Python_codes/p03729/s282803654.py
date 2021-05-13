x = input()
ls_x = x.split()

a = ls_x[0]
b = ls_x[1]
c = ls_x[2]


if a[-1] == b[0] and b[-1] == c[0]:
    print("YES")
else:
    print("NO")