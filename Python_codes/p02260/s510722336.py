def selectionSort(a, n):
    count = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
        count += 1 if i != minj else  0
    return count

def show(a, n):
    for i in range(n):
        if i == n-1:
            print "%d" % a[i]
        else:
            print "%d" % a[i],

n = input()
a = map(int, raw_input().split())
c = selectionSort(a, n)
show(a, n)
print "%d" % c