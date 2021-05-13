def libra(l,r):
    if l>r:
        return "Left"
    elif l == r:
        return "Balanced"
    else:
        return "Right"
def sum(a,b):
    c = a+b
    return c
a,b,c,d=[int(i) for i in input().split()]
print(libra(sum(a,b),sum(c,d)))