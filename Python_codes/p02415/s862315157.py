def check(x):
    if x.islower():
        return x.upper()
    return x.lower()

print ''.join(map(check, map(str, raw_input())))
# use it 'swapcase' then it's easily