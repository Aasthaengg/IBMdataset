def sort(a):
    n = len(a)
    nswaps = 0
    for i in range(n):
        minv = None
        minp = -1
        for j in range(i, n):
            if minv == None or minv > a[j]:
                minv = a[j]
                minp = j
        a[minp], a[i] = a[i], a[minp]
        if i != minp:
            nswaps += 1
    return nswaps

n = int(raw_input())
a = map(int, raw_input().split(' '))
nswaps = sort(a)
print ' '.join(map(str, a))
print nswaps