global_count = 0

def sort(a):
    return merge_sort(a)

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    lo = 0
    hi = n
    med = (lo+hi)/2
    left = merge_sort(a[lo:med])
    right = merge_sort(a[med:hi])
    return merge(left, right)

def merge(a,b):
    global global_count
    c = []
    na = len(a)
    nb = len(b)
    i = 0
    j = 0
    while i < na and j < nb:
        if a[i] < b[j]:
            global_count += 1
            c.append(a[i])
            i += 1
        else:
            global_count += 1
            c.append(b[j])
            j += 1

    if i == na:
        while j < nb:
            global_count += 1
            c.append(b[j])
            j += 1
    if j == nb:
        while i < na:
            global_count += 1
            c.append(a[i])
            i += 1

    return c

n = int(raw_input())
a = map(int, raw_input().split(' '))
c = sort(a)
print ' '.join(map(str, c))
print global_count