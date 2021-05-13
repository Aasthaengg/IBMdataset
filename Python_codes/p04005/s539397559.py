if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    flag = False
    a.sort()
    for i in a:
        if i %2 == 0:
            flag=True
    if flag:
        print(0)
    else:
        print(a[0]*a[1])