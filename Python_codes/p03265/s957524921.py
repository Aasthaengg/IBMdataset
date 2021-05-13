if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    x=a[2]-a[0]
    y=a[3]-a[1]

    print(str(a[2]-y)+" "+ str(a[3]+x)+" "+str(a[0]-y)+" "+str(a[1]+x)+" ")