if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    a11 = a[1]
    a12=a11+a[0]

    a21 = a[2]
    a22 = a21 + a[0]

    if (a11 <= a21 and a12 >= a21) or (a11 <= a22 and a12 >= a22):
        print(0)
    elif a11 <= a21 and a22 <=a22:
        print(abs(a12 -a21))
    else:
        print(abs(a11-a22))