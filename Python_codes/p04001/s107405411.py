def gen(s):
    yield int(s)
    for i in range(len(s)-1):
        l = s[:i+1]
        r = s[i+1:]
        x = int(l)
        for y in gen(r):
            yield x + y
s = input()
print(sum(gen(s)))