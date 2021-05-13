slist = raw_input().split(" ")

def conv_char(c):
    if c.isupper(): return c.lower()
    return c.upper()
    
print " ".join(["".join([conv_char(c) for c in s]) for s in slist])