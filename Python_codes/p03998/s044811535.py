a = list(input())
b = list(input())
c = list(input())
x = "d"
a_idx = 0
b_idx = 0
c_idx = 0
while True:
    if x == "a":
        if a_idx == len(a):
            print("A")
            break
        else:
            x = str(a[a_idx])
            a_idx += 1
    elif x == "b":
        if b_idx == len(b):
            print("B")
            break
        else:
            x = str(b[b_idx])
            b_idx += 1
    elif x == "c":
        if c_idx == len(c):
            print("C")
            break
        else:
            x = str(c[c_idx])
            c_idx += 1
    else:
        x = "a"