def insertionSort(*args):
    l = list(args)
    print ' '.join(map(str, l))
    for i in range(1, n):
        v = l[i]
        j = i - 1
        while j >= 0 and l[j] > v:
            l[j + 1] = l[j]
            j -= 1
            l[j + 1] = v
        print ' '.join(map(str, l))

n = input()
l = map(int, raw_input().split())
insertionSort(*l)