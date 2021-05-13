from itertools import cycle, islice

def fmt(t, o, l):
    i = o % l
    return "".join(islice(cycle(t), i, i+l))

def reader():
    target, offset, length, n = "", 0, 0, -1
    while True:
        s = input()
        if s == "-":
            if target != "":
                yield fmt(target, offset, length)
            break

        if s[0].isalpha():
            if target != "":
                yield fmt(target, offset, length)
            target, offset, length, n = s, 0, len(s), -1            
        else:
            if n < 0:
                n = int(s)
            else:
                offset += int(s)

for s in reader():
    print(s)