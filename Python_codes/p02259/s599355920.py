def bubblesort(a):
    count = 0
    swap = True
    while swap:
        swap = False
        for j in range(1,len(a))[::-1]:
            if a[j] < a[j-1]:
                ret = a[j]
                a[j] = a[j-1]
                a[j-1] = ret
                count += 1
                swap = True           
    print(" ".join(map(str,a)))
    print(count)
    
n = int(input())
a = list(map(int,input().split()))
bubblesort(a)