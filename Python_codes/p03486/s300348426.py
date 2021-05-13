def calculate(s, t):
    a = sorted(s)
    b = sorted(t,reverse=True)

    m = "".join(a)
    k = "".join(b)

    if m < k:
        print("Yes")
    else:
        print("No")


# s = 'yx'
# t = 'axy'
#
# s = 'ratcode'
# t = 'atlas'
#
# s = 'cd'
# t = 'abc'
#
# s = 'w'
# t = 'ww'

s = input()
t = input()
calculate(s, t)
