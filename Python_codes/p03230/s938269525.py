N = int(input())

def f(limit):
    i = 1
    j = 2
    while True:
        if i > limit:
            break
        yield i
        i += j
        j += 1

def h1(l, n):
    s = 0
    for i in range(n):
        yield l[s:s+i+1]
        s += i+1

def h2(p, l):
    if not l:
        return
    for pp, ll in zip(p, l):
        ll.append(pp)
    h2(l[0], l[1:])

l = list(f(10**5))

if N in l:
    print("Yes")

    n = l.index(N)+1
    print(N*2//n)

    t = list(h1(list(range(1, N+1)), n))
    t.reverse()
    t.append([])

    h2(t[0], t[1:])

    for i in t:
        print(len(i), " ".join(str(j) for j in i))
else:
    print("No")
