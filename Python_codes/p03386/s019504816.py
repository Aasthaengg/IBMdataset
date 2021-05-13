if __name__ == '__main__':
    a, b,x = map(int, input().split())
    set1=set([i for i in range(a,min(a+x,b))])
    set2=set([i for i in range(max(a,b-x+1),b+1)])
    sumSet = set1 | set2
    list = list(sumSet)
    list.sort()

    for i in list:
        print(i)
