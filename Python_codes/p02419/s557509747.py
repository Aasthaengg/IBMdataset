import re

def reader():
    p = re.compile("^{}$".format(input()), re.I)
    yield 0
    while True:
        s = input()
        if s == "END_OF_TEXT":
            break
        for w in s.split():
            if p.match(w):
                yield 1

print(sum(reader()))