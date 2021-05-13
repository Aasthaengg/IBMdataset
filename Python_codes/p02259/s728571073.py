def show_list(a):
    for x in a:
        print x,
    print

def bubble_sort(a,n):
    flag = True
    count = 0
    while flag:
        flag = False
        for j in reversed(xrange(1,n)):
            if a[j] < a[j-1]:
                tmp = a[j]
                a[j] = a[j-1]
                a[j-1] = tmp
                count+=1
                flag = True
    show_list(a)
    print count
def main():
    n = input()
    a = map(int,raw_input().split())
    bubble_sort(a,n)

if __name__ == '__main__':
    main()