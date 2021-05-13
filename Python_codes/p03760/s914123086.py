from itertools import zip_longest

O = input()
E = input()

for o, e in zip_longest(O, E, fillvalue=""):
    print(o + e, end="")
