def toggle(c):
    L = c.lower()
    if c == L:
        return c.upper()
    else:
        return L
print(''.join(map(toggle, input())))