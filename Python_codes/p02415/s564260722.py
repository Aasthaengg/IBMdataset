f = lambda c: c.swapcase() if c.isalpha() else c 


print("".join([f(c) for c in input()]))


