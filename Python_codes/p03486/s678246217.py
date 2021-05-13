aa = input()
bb = input()

a = list(aa)
b = list(bb)

a.sort()
b.sort()

b = b[::-1]

S="".join(a)
T="".join(b)


if S<T:
    message = "Yes"
    print(message)
else:
    message = "No"
    print(message)