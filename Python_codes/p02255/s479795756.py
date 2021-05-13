def sort(a):
    n = len(a)
    for i in range(1,n):
        for j in range(i):
            p = i-j
            if a[p] < a[p-1]:
                a[p], a[p-1] = a[p-1], a[p]
        print ' '.join(map(str, a))

n = int(raw_input())
a = map(int, raw_input().split(' '))
print ' '.join(map(str, a))
sort(a)