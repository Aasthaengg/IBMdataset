n = int(input())
l = input()
l = l.split()
a = 0
b = 1
c = 2
e = [0]
for d in range(int(n*(n-1)*(n-2)/6)):
    e.append(int(l[a]))
    e.append(int(l[b]))
    e.append(int(l[c]))
    if b == n - 2 and c == n - 1:
        a = a + 1
        b = a + 1
        c = a + 2
    elif c == n - 1:
        b = b + 1
        c = b + 1
    else:
        c = c + 1
j = 0
for f in range(int((len(e)-1)/3)):
    g = e[f*3+1]
    h = e[f*3+2]
    i = e[f*3+3]
    if g != h and h != i and g != i:
        if g + h > i and h + i > g and g + i > h:
            j = j + 1
print(j)