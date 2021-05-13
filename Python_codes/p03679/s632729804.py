if __name__ == '__main__':
    a = [int(i) for i in input().split()]

    if a[2] <=a[1]:
        print("delicious")
    elif a[2] <= a[0]+a[1]:
        print("safe")
    else:
        print("dangerous")
