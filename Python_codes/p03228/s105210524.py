if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    flag = 0
    for i in range(a[2]):
        count=0
        if flag == 0:
            if a[0] %2 ==1:
                a[0]-=1
            a[0]=a[0]//2
            a[1]+=a[0]
            flag=1
        else:
            if a[1] %2 ==1:
                a[1]-=1
            a[1]=a[1]//2
            a[0]+=a[1]
            flag=0
    print(str(a[0])+" "+str(a[1]))

