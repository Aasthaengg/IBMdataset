s = input().strip()
l = len(s)

def f(s,c,l,v=1):
    n = 0
    for i in range(l-1):
        if s[i] != c:
            if s[i+1] == c:
                s = s[:i] + c + s[i+1:]
                n += 1
        else:
            n += 1
    # print(s[:-1],v)
    if n < l-1:
        return f(s[:-1], c, l-1, v+1)
    else:
        return v

if s.count(s[0]) == l:
    print(0)
    exit()

min = l 
for i in set(s):
    x = f(s, i, l)
    if min > x:
        min = x
print(min)
