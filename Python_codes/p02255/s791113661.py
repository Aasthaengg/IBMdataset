def insertionSort(a, n):
    for i in range(1, n):
        show(a, n)
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = v
    else:
        show(a, n)

def show(a, n):
    for i in range(n):
        if i == n-1:
            print "%d" % a[i]
        else:
            print "%d" % a[i],

n = input()
a = map(int, raw_input().split())
insertionSort(a, n)