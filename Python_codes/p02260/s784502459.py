def show_list(a):
    for x in a:
        print x,
    print

def selection_sort(a,n):
    count=0
    for i in xrange(n):
        minj = i
        for j in xrange(i,n):
            if a[j]<a[minj]:
                minj = j
        if minj!=i:  
            tmp = a[i]
            a[i]=a[minj]
            a[minj]=tmp
            count+=1
    show_list(a)
    print count


def main():
    n = input()
    a = map(int,raw_input().split())
    selection_sort(a,n)


if __name__ == '__main__':
    main()